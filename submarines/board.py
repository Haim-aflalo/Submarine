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
    return x <= size >= y


def count_remaining_ships(ships: list[list[int]], shots: list[list[bool]]) -> int:
    count = 0
    for i in range(len(ships)):
        for j in range(len(ships)):
            if ships and not shots :
                count += 1
    return count
def render_public(ships: list[list[int]], shots: list[list[bool]]) -> str:
    reveal_game = ""
    for i in range(len(ships)):
        for j in range(len(ships)):
            if ships[i][j] and shots[i][j]:
                reveal_game += "V"
            elif not ships[i][j] and shots[i][j]:
                reveal_game += "X"
            else:
                reveal_game += "O"
        reveal_game += "\n"
    return reveal_game























def render_public(ships: list[list[int]], shots: list[list[bool]]) -> str:
    reveal_game = ""
    for i in range(len(ships)):
        for j in range(len(ships)):
            if ships[i][j] and shots[i][j]:
                reveal_game += "V"
            elif not ships[i][j] and shots[i][j]:
                reveal_game += "X"
            else:
                reveal_game += "O"
        reveal_game += "\n"
    return reveal_game


def render_reveal(ships: list[list[int]], shots: list[list[bool]]) -> str:
    pass
