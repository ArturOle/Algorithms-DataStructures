class Error(Exception):
    """
    Base class for exceptions
    """
    pass


class TypeNotNpArray(Error):
    """
    Raised when Inject.from_numpy_array input type is not matching numpy.array

    :parameter imputed:  invalid object inserted as an argument
    :argument message:  information for the user about the error
    """
    def __init__(self, imputed):
        self.imputed = imputed
        self.message = " Imputed object should be an numpy.array "

    def what(self):
        print("Invalid object type: ", self.imputed, self.message)


