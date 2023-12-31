def get_next_position(direction, row, col):
    if direction == 'up':
        return row - 1, col
    elif direction == 'down':
        return row + 1, col


matrix = []
mat = [['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
       ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
       ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
       ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
       ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
       ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
       ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
       ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']]

player = ["White", "Black"]
w_row, w_col = 0, 0
b_row, b_col = 0, 0

for i in range(8):
    matrix.append([el for el in input().split()])
    for j in range(8):
        if matrix[i][j] == 'w':
            w_row, w_col = i, j
        elif matrix[i][j] == 'b':
            b_row, b_col = i, j

while True:
    if player[0] == "White":
        next_row, next_col = get_next_position('up', w_row, w_col)
        if (next_row, next_col + 1) == (b_row, b_col) or (next_row, next_col - 1) == (b_row, b_col):
            print(f"Game over! White win, capture on {mat[b_row][b_col]}.")
            break
        else:
            w_row, w_col = next_row, next_col
            player[0], player[1] = player[1], player[0]
            if w_row == 0:
                print(f'Game over! White pawn is promoted to a queen at {mat[w_row][w_col]}.')
                break
    else:
        next_row, next_col = get_next_position('down', b_row, b_col)
        if (next_row, next_col + 1) == (w_row, w_col) or (next_row, next_col - 1) == (w_row, w_col):
            print(f"Game over! Black win, capture on {mat[w_row][w_col]}.")
            break
        else:
            b_row, b_col = next_row, next_col
            player[0], player[1] = player[1], player[0]
            if b_row == 7:
                print(f'Game over! Black pawn is promoted to a queen at {mat[b_row][b_col]}.')
                break