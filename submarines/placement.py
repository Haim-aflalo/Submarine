import random
def place_random_ships(ships: list[list[int]], n: int)-> None:
    while n > 0:
        col = random.randrange(0,len(ships))
        row = random.randrange(0,len(ships))
        if ships[row][col] == 0:
            ships[row][col] = 1
            n -= 1