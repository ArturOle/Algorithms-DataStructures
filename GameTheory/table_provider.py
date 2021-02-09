import numpy as np
import exceptions


class Inject:
    @classmethod
    def from_input(cls, square_matrix_shape):
        """
        Acquiring input from the user to fill the payoff table.

        :param square_matrix_shape:
        :return numpy.array:
        """
        cls.matrix = np.zeros((square_matrix_shape, square_matrix_shape))

        try:
            """
            Making sure that the imputed data is an digit.
            """
            for i, row in enumerate(cls.matrix):
                for j, val in enumerate(row):
                    val = int(input(" Enter value in position ({}, {}): ".format(j, i)))
                    cls.matrix[i, j] = val
            return cls.matrix
        except ValueError:
            print(" ValueError! Use only integers as the matrix values! ")
            exit(-1)

    @classmethod
    def from_numpy_array(cls, np_array=np.zeros(0)):
        """
        Numpy array injection

        :param np_array:
        :return numpy.array:
        """
        try:
            """
            Making sure that the object is a numpy array.
            """
            if type(np_array) is not np.ndarray:
                raise exceptions.TypeNotNpArray(np_array)
            cls.matrix = np_array
            return cls.matrix

        except exceptions.TypeNotNpArray as TNNA:
            TNNA.what()
            exit(-2)


if __name__ == "__main__":
    matrix1 = Inject.from_input(2)
    # matrix2 = Inject().from_numpy_array(np.array([[1, -1], [3, -3]]))

"""
Error codes:

-1  -  ValueError in Inject.from_input
-2  -  TypeNotNpArray in Inject.from_numpy_array
"""
