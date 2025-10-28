from submarines.board import create_matrix
from submarines.placement import place_random_ships

board = create_matrix(5)
print(board)
place_random_ships(board, 4)

for row in board:
    print(row)