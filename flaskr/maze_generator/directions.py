from enum import Enum


class Directions(Enum):
    N = (-1, -0)
    S = (1, 0)
    E = (0, 1)
    W = (0, -1)
