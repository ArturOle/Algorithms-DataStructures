from Powell import Powell2
from GradCon import GradCon2
from time import sleep
import numpy as np


def function(x, y, a, b):
    return np.exp(np.cos(x-a)) + np.exp(np.cos(y-b))


if __name__ == "__main__":

    powell = Powell2(function, -1, 1, -1, 1)

    powell.find(0.0001)

    gradcon = GradCon2(function, -1, 1, -1, 1)

    s = gradcon.find(0.0001)
    print(s)

    sleep(10)
