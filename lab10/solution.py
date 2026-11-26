import numpy as np

def make_table(rows: int, columns: int) -> list[list[int]]:
    return np.arange(rows * columns).reshape(rows, columns).tolist()
def rectangle(matrix: list[list[float]],row_start: int,row_stop: int,
    column_start: int,column_stop: int,) -> list[list[float]]:
    arr = np.array(matrix)
    return arr[row_start:row_stop, column_start:column_stop].tolist()
def replace_rectangle(matrix: list[list[float]],row_start: int,row_stop: int,
    column_start: int,column_stop: int,value: float,) -> list[list[float]]:
    dtype = float if isinstance(value, float) else None
    arr = np.array(matrix, dtype=dtype).copy()
    arr[row_start:row_stop, column_start:column_stop] = value
    return arr.tolist()
