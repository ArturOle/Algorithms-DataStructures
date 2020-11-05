import numpy as np
import random


class Powell2:
    def __init__(self, function
                 , min_in_x, max_in_x
                 , min_in_y, max_in_y
                 , x_position=1, y_position=-0.5
                 , a_value=-0.8, b_value=0.5):

        self.golden_ratio = (np.sqrt(5) + 1) / 2

        self.range_x = [min_in_x, max_in_x]  # domain for x
        self.range_y = [min_in_y, max_in_y]  # domain for y

        self.main_function = function  # function of 2 variables which is the subject of calculation in form of the string

        self.direction = [1, 0]  # switch for going in x or y direction. Start with x

        self.x = x_position
        self.y = y_position

        self.matrix = [[self.range_x[0], self.range_y[0]], [self.x, self.y]]  # positions positions

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

    def find_move(self, switch=0, tolerance=0.00001):
        if switch == 0:
            trial_x_r = self.range_x[1] - (self.range_x[1] - self.range_x[0]) / self.golden_ratio
            trial_x_l = self.range_x[0] + (self.range_x[1] - self.range_x[0]) / self.golden_ratio

            while abs(self.range_x[1] - self.range_x[0]) > tolerance:

                if self.main_function(trial_x_l, self.y, self.a, self.b) < self.main_function(trial_x_r, self.y, self.a, self.b):
                    self.range_x[1] = trial_x_r

                else:
                    self.range_x[0] = trial_x_l

                print(self.range_x[0], self.range_x[1], self.main_function(self.range_x[0], self.y, self.a, self.b))
                trial_x_r = self.range_x[1] - (self.range_x[1] - self.range_x[0]) / self.golden_ratio

                print(self.range_x[0], self.range_x[1], self.main_function(self.range_x[1], self.y, self.a, self.b))
                trial_x_l = self.range_x[0] + (self.range_x[1] - self.range_x[0]) / self.golden_ratio

            self.x = (trial_x_l + trial_x_r) / 2
            return self.x
        else:
            trial_y_r = self.range_y[1] - (self.range_y[1] - self.range_y[0]) / self.golden_ratio
            trial_y_l = self.range_y[0] + (self.range_y[1] - self.range_y[0]) / self.golden_ratio

            while abs(self.range_y[1] - self.range_y[0]) > tolerance:

                if self.main_function(self.x, trial_y_l, self.a, self.b) < self.main_function(self.x, trial_y_r, self.a, self.b):
                    self.range_y[1] = trial_y_r
                else:
                    self.range_y[0] = trial_y_l

                print(self.range_y[0], self.range_y[1], self.main_function(self.x, self.range_y[0], self.a, self.b))
                trial_y_r = self.range_y[1] - (self.range_y[1] - self.range_y[0]) / self.golden_ratio
                print(self.range_y[0], self.range_y[1], self.main_function(self.x, self.range_y[1], self.a, self.b))
                trial_y_l = self.range_y[0] + (self.range_y[1] - self.range_y[0]) / self.golden_ratio

            self.y = (trial_y_l + trial_y_r)/2
            return self.y

    def find(self, tol):
        new_point = [self.find_move(0, tolerance=tol), self.find_move(1, tolerance=tol,)]

        self.matrix.append(new_point)
        print("\n### Powell ###")
        print("Position x: ", self.matrix[2][0], "Position y: ", self.matrix[2][1], " Value: ", self.main_function(self.matrix[2][0], self.matrix[2][1], self.a, self.b))
        print(self.matrix[2], "\n\n")
