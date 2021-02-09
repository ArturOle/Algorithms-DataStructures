from table_provider import Inject
import numpy as np


class Safe:
    """
    Safe strategies for Zero-sum games

    :param matrix:  Matrix in form of numpy array injected with Inject object
    """

    def __init__(self, matrix=np.zeros(2)):
        self.matrix = matrix

    def show_array(self):
        print("Payoff matrices: \n", self.matrix)

    def safe_strategy(self):
        #  Show the current matrix
        self.show_array()
        #  Search for choices of Player1
        self.player1()
        #  Search for choices of Player2
        self.player2()

    def player1(self):
        #  Transposing the matrix for easier management of the matrix columns
        matrix = self.matrix.T

        #  Initializing and filling options list with possible choices for safe strategies
        #  ( *minimums of the columns* )
        options = []
        for i, column in enumerate(matrix):
            options.append((i + 1, min(column)))
        print("Minimums from columns: \n", options)

        #  From possible choices we choose ones with the highest value as well as the duplicates
        choices = []
        for point in options:
            if len(choices) == 0:
                choices.append(point)
            else:
                for choice in choices:
                    if point[1] > choice[1]:
                        choice = point[1]
                    elif point[1] == choice[1]:
                        choices.append(point)
                        break

        print("Safe Strategy choices for player1: \n", choices)
        return choices

    def player2(self):
        #  Initializing the matrix
        matrix = self.matrix

        #  Searching for the highest values in the rows
        options = []
        for j, row in enumerate(matrix):
            options.append((j + 1, max(row)))
        print("Maximums from rows: \n", options)

        #  From possible choices chose the lowest
        choices = []
        for point in options:
            if len(choices) == 0:
                choices.append(point)
            else:
                for choice in choices:
                    if point[1] < choice[1]:
                        choice = point[1]
                    elif point[1] == choice[1]:
                        choices.append(point)
                        break

        print("Safe Strategy choices for player2: \n", choices)
        return choices


if __name__ == "__main__":
    """
      If you want to input your own table, use Inject.from_input(|Shape here|)
      For more information check table_provider.py
    """
    Safe(Inject.from_numpy_array(np.array([[-2, 6, 8, -6], [4, -8, -4, 8]]))).safe_strategy()
