import numpy as np


def make_hours() -> list[int]:
    arr = np.arange(0, 22, 3)
    return arr.tolist()