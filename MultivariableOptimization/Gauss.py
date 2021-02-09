import math
import numpy as np
import random


class Gauss2:
    def __init__(self, function
                     , min_in_x, max_in_x
                     , min_in_y, max_in_y
                     , x_position=0.1, y_position=0.1
                     , a_value=-0.8, b_value=0.5):

        self.golden_ratio = (np.sqrt(5) + 1)/2
        self.golden_ratio_2 = (3 - math.sqrt(5))/2

        self.range_x = [min_in_x, max_in_x]  # domain for x
        self.range_y = [min_in_y, max_in_y]  # domain for y

        self.function = function  # function of 2 variables which is the subject of calculation in form of the string

        self.search_direction = [1, 0]  # switch for going in x or y direction. Start with x

        self.x = x_position
        self.y = y_position

        self.matrix = [[self.x, self.y], [0, 0]]   # initial positions in x[0]

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

    def step(self, tol):
        for i in range(2):
            if i:
                self.find_move(0, tolerance=tol)
                self.x = (self.range_x[0] + self.range_x[1]) / 2
            else:
                self.find_move(1, tolerance=tol)
                self.y = (self.range_y[0] + self.range_y[1])/2

        print(self.x, self.y)

    def find_move(self, switch, tolerance=0.1):
        if switch == 0:
            trial_x_r = self.range_x[1] - (self.range_x[1] - self.range_x[0]) / self.golden_ratio
            trial_x_l = self.range_x[0] + (self.range_x[1] - self.range_x[0]) / self.golden_ratio

            while abs(self.range_x[1] - self.range_x[0]) > tolerance:

                if self.function(trial_x_l, self.y, self.a, self.b) < self.function(trial_x_r, self.y, self.a, self.b):
                    self.range_x[1] = trial_x_r

                else:
                    self.range_x[0] = trial_x_l

                print(self.range_x[0], self.range_x[1], self.function(self.range_x[0], self.y, self.a, self.b))
                trial_x_r = self.range_x[1] - (self.range_x[1] - self.range_x[0]) / self.golden_ratio

                print(self.range_x[0], self.range_x[1], self.function(self.range_x[1], self.y, self.a, self.b))
                trial_x_l = self.range_x[0] + (self.range_x[1] - self.range_x[0]) / self.golden_ratio

        else:
            trial_y_r = self.range_y[1] - (self.range_y[1] - self.range_y[0]) / self.golden_ratio
            trial_y_l = self.range_y[0] + (self.range_y[1] - self.range_y[0]) / self.golden_ratio

            while abs(self.range_y[1] - self.range_y[0]) > tolerance:

                if self.function(self.x, trial_y_l, self.a, self.b) < self.function(self.x, trial_y_r, self.a, self.b):
                    self.range_y[1] = trial_y_r
                else:
                    self.range_y[0] = trial_y_l

                print(self.range_y[0], self.range_y[1], self.function(self.x, self.range_y[0], self.a, self.b))
                trial_y_r = self.range_y[1] - (self.range_y[1] - self.range_y[0]) / self.golden_ratio
                print(self.range_y[0], self.range_y[1], self.function(self.x, self.range_y[1], self.a, self.b))
                trial_y_l = self.range_y[0] + (self.range_y[1] - self.range_y[0]) / self.golden_ratio
"""

    def find_alpha_derivative(self, var_for_diff=0):
        x, y = symbols("x y", real=True)
        a, b = -0.8, 0.5
        alpha = symbols("alf", real=True)

        print(self.x, self.y)
        if var_for_diff == 0:
            z = self.function(x, y, a, b)
            deriv = Derivative(z, x).doit()
            ans = deriv.subs(x, x + alpha)
            ans = ans.subs(x, self.x)
            sol = solve(ans)

            return sol[0]
        else:
            z = self.function(x, y, a, b)
            deriv = Derivative(z, y).doit()
            ans = deriv.subs(y, y + alpha)
            ans = ans.subs(y, self.y)
            sol = solve(ans)

            return sol[0]
""""""
Begin
   Take the dimensions of the matrix p and its elements as input.
   Take the initials values of x and no of iteration q as input.
   While q>0
      Make a for loop i = 0 to p-1
         initialize n[i] = (b[i] / a[i][i]).
            Make a for loop i = 0 to p-1
            If (j == i)
               n[i] = n[i] - ((a[i][j] / a[i][i]) * m[j]).
               m[i] = n[i].
      Decrease q.
   /*
      Here, a[i][j] = input matrix.
      b[i] = this array takes values of the right side of equation.
      m[i] = stores initial values of x.
   */
   Return 0
End
"""
