import numpy as np
import random


class GradCon2:
    def __init__(self, function
                 , min_in_x, max_in_x
                 , min_in_y, max_in_y
                 , x_position=0.1, y_position=0.1
                 , a_value=-0.8, b_value=0.5):
        self.golden_ratio = (np.sqrt(5) + 1) / 2

        self.range_x = (min_in_x, max_in_x)  # domain for x
        self.range_y = (min_in_y, max_in_y)  # domain for y

        self.main_function = function  # function of 2 variables which is the subject of calculation in form of the string

        self.search_direction = [1, 0]  # switch for going in x or y direction. Start with x

        self.x = x_position
        self.y = y_position

        self.lines = [[[self.x, self.y], [self.x + 0.1 * min_in_x, self.y]]
                    , [[self.x, self.y], [self.x - 0.1 * min_in_x, self.y]]]

        self.matrix = [[self.x, self.y], [0, 0]]  # initial positions in x[0]

        self.a = a_value  # arguments
        self.b = b_value

        self.initial_check()

        self.alpha = 0
        # print(self.range_x[0], self.range_x[1])
        self.current_iteration = 1  # variable keeping track of the current iteration

    def initial_check(self):
        if self.range_x[0] >= self.x >= self.range_x[1]:
            self.x = random.uniform(self.range_x[0], self.range_x[1])

        if self.range_y[0] >= self.y >= self.range_y[1]:
            self.y = random.uniform(self.range_y[0], self.range_y[1])

    def line(self, point_a, point_b, var, mode=1):
        a = point_b[0] - point_a[0]
        b = point_b[1] - point_a[1]
        if mode == 1:
            if b == 0:
                return var
            else:
                slope = a/b
                return slope*(var + point_a[0]) + point_a[1]
        else:
            if a == 0:
                return var
            else:
                slope = b/a
                return slope*(var - point_a[1]) - point_a[0]

    def find_max_point(self, point_one, point_two, tolerance=0.00001, mode=0):

        if mode == 0:
            iteration_range = list(self.range_x)
            trial_x_r = iteration_range[1] - (iteration_range[1] - iteration_range[0]) / self.golden_ratio
            trial_x_l = iteration_range[0] + (iteration_range[1] - iteration_range[0]) / self.golden_ratio

            while abs(iteration_range[1] - iteration_range[0]) > tolerance:

                if (self.main_function(trial_x_l, self.line(point_one, point_two, trial_x_l, mode=0), self.a, self.b)
                   < self.main_function(trial_x_r, self.line(point_one, point_two, trial_x_r, mode=0), self.a, self.b)):

                    iteration_range[1] = trial_x_r
                else:
                    iteration_range[0] = trial_x_l

                print(iteration_range[0], iteration_range[1], self.main_function(trial_x_r, self.line(point_one, point_two, trial_x_r, 0), self.a, self.b))
                trial_x_r = iteration_range[1] - (iteration_range[1] - iteration_range[0]) / self.golden_ratio
                print(iteration_range[0], iteration_range[1], self.main_function(trial_x_l, self.line(point_one, point_two, trial_x_l, 0), self.a, self.b))
                trial_x_l = iteration_range[0] + (iteration_range[1] - iteration_range[0]) / self.golden_ratio

            self.x = (trial_x_l + trial_x_r) / 2
            return self.x

        else:
            iteration_range = list(self.range_y)
            trial_y_r = iteration_range[1] - (iteration_range[1] - iteration_range[0]) / self.golden_ratio
            trial_y_l = iteration_range[0] + (iteration_range[1] - iteration_range[0]) / self.golden_ratio

            while abs(iteration_range[1] - iteration_range[0]) > tolerance:
                if (self.main_function(self.line(point_one, point_two, trial_y_l, mode=0), trial_y_l, self.a, self.b)
                   < self.main_function(self.line(point_one, point_two, trial_y_r, mode=0), trial_y_r, self.a, self.b)):

                    iteration_range[1] = trial_y_r
                else:
                    iteration_range[0] = trial_y_l

                print(iteration_range[0], iteration_range[1], self.main_function(trial_y_r, self.line(point_one, point_two, trial_y_r), self.a, self.b))
                trial_y_r = iteration_range[1] - (iteration_range[1] - iteration_range[0]) / self.golden_ratio
                print(iteration_range[0], iteration_range[1], self.main_function(trial_y_l, self.line(point_one, point_two, trial_y_l), self.a, self.b))
                trial_y_l = iteration_range[0] + (iteration_range[1] - iteration_range[0]) / self.golden_ratio

            self.y = (trial_y_l + trial_y_r) / 2
            return self.y

    def find(self, tol=0.0001):
        conjugate_line = []
        for i in range(len(self.lines)):
            conjugate_line.append([self.lines[i][1][0], self.find_max_point(self.lines[i][0], self.lines[i][1], mode=1)])

        self.lines.append(conjugate_line)
        maximum_point = [self.find_max_point(conjugate_line[0], conjugate_line[1], mode=0), conjugate_line[1][1]]

        print("\n\n### Gradient Conjugate ###\nPosition x: ", maximum_point[0], "Position y: ", maximum_point[1], " Value: ", self.main_function(maximum_point[0],maximum_point[1], self.a, self.b))
        print("Lines: ", self.lines)
        return maximum_point
