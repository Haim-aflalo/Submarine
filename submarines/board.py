def create_matrix(size: int, fill: int = 0):
    mat = []
    for i in range(size):
        lst = []
        for j in range(size):
            lst.append(fill)
        mat.append(lst)
    return mat

def create_bool_matrix(size: int, fill: bool = False):
    mat = []
    for i in range(size):
        lst = []
        for j in range(size):
            lst.append(fill)
        mat.append(lst)
    return mat

def in_bounds(size: int, x: int, y: int):
    if x <= size >= y:
        return True
    else:
        return False

def count_remaining_ships(ships: list[list[int]], shots: list[list[bool]]) -> int:
    count = 0
    for i in range(len(ships)):
        for j in range(len(ships)):
            if ships and not shots :
                count += 1
    return count

