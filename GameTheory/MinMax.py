import numpy as np
from table_provider import Inject


class MinMax:
    """
    Implementation of Nash Equilibrium

    :parameter matrix_p1:   pay-off matrix for player1
    :parameter matrix_p2:   pay-off matrix for player2
    :returns choices:       returns minmax strategies
    """
    def __init__(self, matrix_p1=np.zeros(2), matrix_p2=np.zeros(2)):
        self.matrixP1 = matrix_p1
        self.matrixP2 = matrix_p2

    def show_array(self):
        print("Pay-off matrix of player1: \n", self.matrixP1)
        print("Pay-off matrix of player2: \n", self.matrixP2)

    def minmax(self):
        """
        :return nash_equilibrium:  the minmax strategy found in the pay-off tables
        """
        self.show_array()
        p1_options = self.player1()
        p2_options = self.player2()
        minmax_strategy = self.joint(p1_options, p2_options)
        return minmax_strategy

    def player1(self):
        #  Searching for minimum values for every column
        matrix = self.matrixP1.T

        options = []
        for i, column in enumerate(matrix):
            value = min(column)
            options.append([i, min(column)])

        print("Options of player1: \n", options)
        return options

    def player2(self):
        #  Searching for minimum values for every row
        matrix = self.matrixP2

        options = []
        for i, row in enumerate(matrix):
            value = max(row)
            options.append([i, max(row)])

        print("Options of player2: \n", options)
        return options

    def joint(self, p1_options, p2_options):
        max_p1 = [0, -np.inf]
        max_p2 = [0, np.inf]
        for val in p1_options:
            if max_p1[1] < val[1]:
                max_p1 = val
        for val in p2_options:
            if max_p2[1] > val[1]:
                max_p2 = val

        print("Minmax strategy: \n", [max_p1[0], max_p2[0]])
        return [max_p1[0], max_p2[0]]


if __name__ == "__main__":
    """
      If you want to input your own table, use Inject.from_input(|Shape here|)
      For more information check table_provider.py
    """
    game = MinMax(Inject.from_numpy_array(np.array([[-4, 3, -2], [3, -5, 8], [5, -1, -2]])),
                  Inject.from_numpy_array(np.array([[-1, 4, 1], [3, -8, -3], [4, 6, -7]])))

    game.minmax()

