import numpy as np
from table_provider import Inject


class Nash:
    """
    Implementation of Nash Equilibrium

    :parameter matrix_p1:   pay-off matrix for player1
    :parameter matrix_p2:   pay-off matrix for player2
    :returns choices:       possible choices gathered with Nash Equilibrium procedure
    """
    def __init__(self, matrix_p1=np.zeros(2), matrix_p2=np.zeros(2)):
        self.matrixP1 = matrix_p1
        self.matrixP2 = matrix_p2

    def show_array(self):
        print("Pay-off matrix of player1: \n", self.matrixP1)
        print("Pay-off matrix of player2: \n", self.matrixP2)

    def safe_equilibrium(self):
        """
        :return nash_equilibrium:  list of Nash Equilibriums found in the pay-off tables
        """
        self.show_array()
        p1_options = self.player1()
        p2_options = self.player2()
        nash_equilibrium = self.joint(p1_options, p2_options)
        return nash_equilibrium

    def player1(self):
        #  Searching for minimum values for every column
        matrix = self.matrixP1.T

        options = []
        for i, column in enumerate(matrix):
            value = min(column)
            for j, matrix_val in enumerate(column):
                if matrix_val == value:
                    options.append([i, j, min(column)])
        print("Options of player1: \n", options)
        return options

    def player2(self):
        #  Searching for minimum values for every row
        matrix = self.matrixP2

        options = []
        for i, row in enumerate(matrix):
            value = min(row)
            for j, matrix_val in enumerate(row):
                if matrix_val == value:
                    options.append([i, j, min(row)])
        print("Options of player1: \n", options)
        return options

    def joint(self, p1_options, p2_options):
        #  Merging p1_options and p2_options ( from ((1,1), 3) and ((1,1), -4) to ((1,1), 3, -4) )
        choices = []
        for choice_p1 in p1_options:
            for choice_p2 in p2_options:
                if choice_p1[0] == choice_p2[0] and choice_p1[1] == choice_p2[1]:
                    choices.append((choice_p1[0:2], choice_p1[2], choice_p2[2]))
        print("Choices: \n", choices)
        return choices

    def best_choice(self, flag="min"):
        #  Acquiring the safe equilibriums from the tables
        choices = self.safe_equilibrium()

        #  If user is searching for lowest cost it uses the min
        if flag == "min":
            #  Initializing with list of tuple and two values which will be
            #  our variables to be minimized
            curr_min = [(), np.inf, np.inf]

            #  For every choice we calculate the sum from two pay-off tables and
            #  compare it to the current curr_min
            for choice in choices:
                if (choice[1] + choice[2]) < (curr_min[1] + curr_min[2]):
                    #  If sum of choice values is lower then sum of curr_min values
                    #  then curr_min is equal to this choice
                    curr_min = choice

            print("Best choice if we're searching for minimum: \n", curr_min)
            return curr_min

        #  If user is searching for highest income it uses the max
        elif flag == "max":
            #  Initializing with list of tuple and two values which will be
            #  our variables to be maximized
            curr_max = [(), -np.inf, -np.inf]

            #  For every choice we calculate the sum from two pay-off tables and
            #  compare it to the current curr_min
            for choice in choices:
                if (choice[1] + choice[2]) > (curr_max[1] + curr_max[2]):
                    #  If sum of choice values is higher then sum of curr_min values
                    #  then curr_min is equal to this choice
                    curr_max = choice

            print("Best choice if we're searching for max: \n", curr_max)
            return curr_max


if __name__ == "__main__":
    """
      If you want to input your own table, use Inject.from_input(|Shape here|)
      For more information check table_provider.py
    """
    game = Nash(Inject.from_numpy_array(np.array([[-4, 3, -2], [3, -5, 8], [5, -1, -2]])),
                Inject.from_numpy_array(np.array([[-1, 4, 1], [3, -8, -3], [4, 6, -7]])))

    game.safe_equilibrium()
    game.best_choice(flag="min")
    game.best_choice(flag="max")

