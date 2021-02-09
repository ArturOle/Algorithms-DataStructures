from table_provider import Inject
import numpy as np


class Stackelberg:
    """
    Implementation of von Stackelberg equilibrium

    :parameter matrix_p1:   pay-off matrix for player1
    :parameter matrix_p2:   pay-off matrix for player2
    :returns choice:       choice gathered with von Stackleberg Equilibrium
    """

    def __init__(self, matrix_p1=np.zeros(2), matrix_p2=np.zeros(2)):
        self.matrixP1 = matrix_p1
        self.matrixP2 = matrix_p2

    #  Method responsible for presentation of rational responses
    def show(self, responses):
        print("Pay-off matrix of player1: \n", self.matrixP1)
        print("Pay-off matrix of player2: \n", self.matrixP2)
        print("Rational responses: ")
        for i, decision in enumerate(responses):
            print("\tR{} = {position} = {value} ".format(i, position=decision[0][1], value=decision[1]))

    def rational_responses(self):
        matrix_p1 = self.matrixP1.T

        #  Searching for coordinates of rational responses
        choices = []
        for i, row in enumerate(matrix_p1):
            choice = (None, np.inf)
            for j, column in enumerate(self.matrixP2):
                if choice[1] > self.matrixP2[i][j]:
                    choice = ((i, j), self.matrixP2[i][j])
            choices.append(choice)
        return choices

    def stackelberg(self):
        rational = self.rational_responses()
        self.show(rational)
        choice = self.decision(rational)
        self.result(rational, choice)

    def decision(self, rational):
        #  Choosing best choice(maximal vaule) for Leader (player1)
        coordinates = [data[0] for data in rational]
        choices = [self.matrixP1[coord[0], coord[1]] for coord in coordinates]
        choice = [coordinates[choices.index(max(choices))], max(choices)]
        print("Decision of the leader: \n\t", choice)
        return choice

    def result(self, rational, choice):
        # Presentation of the choice and values for the players
        print("Coordinates: \n\t", choice[0])
        for coord in rational:
            if coord[0] == choice[0]:
                print("Values: "
                      "\n\tPlayer1:\n\t\t", choice[1],
                      "\n\tPlayer2:\n\t\t", coord[1])


if __name__ == "__main__":
    """
      If you want to input your own table, use Inject.from_input(|Shape here|)
      For more information check table_provider.py
    """
    game = Stackelberg(Inject.from_numpy_array(np.array([[-4, 3, -2], [3, -5, 8], [5, -1, -2]])),
                       Inject.from_numpy_array(np.array([[-1, 4, 1], [3, -8, -3], [4, 6, -7]])))

    game.stackelberg()
