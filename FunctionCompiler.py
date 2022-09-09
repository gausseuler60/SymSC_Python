import numpy as np
from scipy import linalg


class FunctionCompiler:

    def __init__(self, object_list, t):
        self._check_time(t)
        self.h = h = t[1] - t[0]
        self.time = np.array(t)
        self.object_list = object_list
        left_matrix_list = []

        # TODO add complex object support
        self._assign_data_index()
        object_list = self.object_list
        for obj in object_list:
            if obj.data_index is None:
                obj.data_index = obj.loc

        # system sizes
        # 1. number of currents
        self.m = 0
        # 2. number of nodes - just the maximal value of data_index
        self.n = max([max(i.data_index) for i in object_list])
        # 3. number of elements with an additional variable - contains 4 rows (or 3, if grounded)
        self.i = 0

        curr_index_now = 0
        var_index_now = 0
        for i, o in enumerate(object_list):
            matrix_stamp = o.get_matrix_stamp(h)
            o.data_index = o.loc

            if o.contains_current:  # if it is a current source, it contains only 2 variables (or 1, if grounded)
                self.m += 1
                o.current_index = curr_index_now
                curr_index_now += 1
            else:
                o.current_index = -1

            if o.contains_variable:  # if it is a Josephson, it contains 4 variables (or 3, if grounded)
                self.i += 1
                o.var_index = var_index_now
                var_index_now += 1
            else:
                o.var_index = -1

            left_matrix_list.append(matrix_stamp)
        # variables in x vector:
        # 1) n phases
        # 2) i variables
        # 3) m currents
        for obj in object_list:
            if obj.current_index != -1:
                obj.current_index += (self.n + self.i)  # voltages -> vars -> currents
            if obj.var_index != -1:
                obj.var_index += self.n  # voltages -> vars

        self._left_matrix_list = left_matrix_list
        self._create_matrix()

    @staticmethod
    def _check_time(time):
        td = time[1:] - time[:-1]
        if not (np.all(td - td[0] < 1e-9) and np.all(td > 0)):
            raise ValueError('Time must be monotonically increasing and evenly spaced')

    def _assign_data_index(self):
        index_dict = {}
        complex_objects = []
        complex_obj_indices = []
        N = 0

        for i, obj in enumerate(self.object_list):
            # make an unique number sequence in names for each object type
            if obj.name in index_dict:
                index_dict[obj.name] += 1
                numb = index_dict[obj.name]
            else:
                index_dict[obj.name] = 1
                numb = 1

            obj.name = f"{obj.name}{numb}"  # make one-based numbering
            obj.data_index = obj.loc

            if obj.complex:
                complex_objects.append(obj)
                complex_obj_indices.append(i)

            if N < max(obj.loc):
                N = max(obj.loc)

        self.N = N

        # generate DataIndex for complex objects
        # in a complex object, first 2 (sometimes 1) DataIndex are input and output,
        # and other ones must be generated
        for comp_obj in complex_objects:
            n_this = comp_obj.N
            pins = len(comp_obj.loc)

            new_data_index = np.zeros(n_this - pins, dtype=int)
            if n_this > pins:
                for p in range(0, n_this - pins):
                    self.N += 1
                    new_data_index[p] = self.N
                comp_obj.data_index.extend(new_data_index)

        # unzip complex objects
        for i, comp_obj in zip(complex_obj_indices, complex_objects):
            # generate child objects for this object
            new_names_obj = comp_obj.unzip()
            self.object_list[i] = None
            self.object_list.extend(new_names_obj)

        self.object_list = [obj for obj in self.object_list if not (obj is None)]

        self.object_dict = {obj.name: obj for obj in self.object_list}
        self._assigned = True

        print('Generated objects are:', " ".join(self.object_dict.keys()))

    def _get_obj_row_indices(self, obj):
        this_obj_row_indices = []

        if obj.data_index[0] != 0:
            row_vp = obj.data_index[0] - 1
            this_obj_row_indices.append(row_vp)
        if obj.data_index[1] != 0:
            row_vm = obj.data_index[1] - 1
            this_obj_row_indices.append(row_vm)
        if obj.var_index != -1:
            row_var = obj.var_index
            this_obj_row_indices.append(row_var)
        if obj.current_index != -1:
            row_current = obj.current_index
            this_obj_row_indices.append(row_current)

        return this_obj_row_indices

    def _create_matrix(self):
        size = self.m + self.n + self.i
        final_A = np.zeros((size, size))
        for obj, matr in zip(self.object_list, self._left_matrix_list):
            print(obj.name, obj.data_index)
            # define indices into what we must place matrix elements
            this_obj_row_indices = self._get_obj_row_indices(obj)
            # now place them:
            for i in range(len(this_obj_row_indices)):
                for j in range(len(this_obj_row_indices)):
                    final_A[this_obj_row_indices[i], this_obj_row_indices[j]] += matr[i, j]

        self.A = final_A

    def solve(self, y0=None):
        size = self.m + self.n + self.i
        h = self.h
        A = self.A
        t_max = np.max(self.time)

        if y0 is None:
            y0 = np.zeros(size)

        n_time_steps = int(t_max / h)
        sol = np.zeros((size, n_time_steps + 1))
        time = np.zeros(n_time_steps + 1)
        sol[:, 0] = y0

        i_step = 0

        while i_step <= n_time_steps:
            # print(i_step, n_time_steps)
            B_this_step = np.zeros(size)
            for obj in self.object_list:
                b = obj.get_right_side(sol, i_step, h)
                indices = self._get_obj_row_indices(obj)
                for bi, idx in zip(b, indices):
                    B_this_step[idx] += bi
            # print(B_this_step)
            x_now = linalg.solve(A, B_this_step)
            # print('x', x_now)
            sol[:, i_step] = x_now
            time[i_step] = i_step * h
            i_step += 1

        return sol
