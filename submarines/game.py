import board
import placement


def init_game(size,n_ships, max_shots,*, rng) ->dict:
    ship = board.create_matrix(size)
    ship_mat = placement.place_random_ships(ship,n_ships)
    shot_mat = board.create_bool_matrix(size)
    state = {"size":size,"ships":ship_mat,"shots":shot_mat,"n_ships":n_ships,"max_shots":max_shots,"rng":rng}
    return state
def shoot(state: dict, x: int, y: int) -> tuple[bool, str]:
    is_hit = False
    if board.is_bounds(x,y):
        if state["ships"][x][y] == 1:
            return True, "Great you hit a boat !"
        else:
            return False,"Nothing here!"