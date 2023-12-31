def get_next_position(direction, r, c):
    if direction == 'up':
        if r-1 < 0:
            r = row-1
        else:
            r -= 1
    elif direction == 'down':
        if r+1 == row:
            r = 0
        else:
            r += 1
    elif direction == 'left':
        if c-1 < 0:
            c = col-1
        else:
            c -= 1
    elif direction == 'right':
        if c+1 == col:
            c = 0
        else:
            c += 1
    return r, c


row, col = eval(input())
matrix = []
santa_row, santa_col = 0, 0
presents = 0
items = {'D': 0, 'G': 0, 'C': 0}

for i in range(row):
    matrix.append([el for el in input().split()])
    for j in range(col):
        if matrix[i][j] == "Y":
            santa_row, santa_col = i, j
        elif matrix[i][j] in ("D", "G", "C"):
            presents += 1

while presents != 0:
    command = input().split('-')
    if command[0] == "End":
        break
    else:
        direction, steps = command[0], int(command[1])
        for i in range(steps):
            next_row, next_col = get_next_position(direction, santa_row, santa_col)
            if matrix[next_row][next_col] in ('G', 'C', 'D'):
                presents -= 1
                items[matrix[next_row][next_col]] += 1
            matrix[santa_row][santa_col] = 'x'
            santa_row, santa_col = next_row, next_col
            matrix[santa_row][santa_col] = 'Y'
            if presents == 0:
                print("Merry Christmas!")
                break

print("You've collected:")
for k, v in items.items():
    if k == 'D':
        print(f'- {v} Christmas decorations')
    elif k == 'G':
        print(f'- {v} Gifts')
    elif k == 'C':
        print(f'- {v} Cookies')

[print(*row) for row in matrix]