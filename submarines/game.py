import board
import placement


def init_game(size,n_ships, max_shots,*, rng) ->dict:
    ship = board.create_matrix(size)
    ship_mat = placement.place_random_ships(ship,n_ships)
    shot_mat = board.create_bool_matrix(size)
    state = {"size":size,"ships":ship_mat,"shots":shot_mat,"n_ships":n_ships,"max_shots":max_shots,"rng":rng}
    return state
