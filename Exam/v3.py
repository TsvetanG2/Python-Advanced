def find_mouse(matrix):
    rows, cols = len(matrix), len(matrix[0])
    mouse_pos = None
    cheese_count = 0
    trap_pos = None

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 'M':
                mouse_pos = (r, c)
            elif matrix[r][c] == 'C':
                cheese_count += 1
            elif matrix[r][c] == 'T':
                trap_pos = (r, c)

    return mouse_pos, cheese_count, trap_pos


def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))


def move_mouse(matrix, direction, mouse_pos):
    rows, cols = len(matrix), len(matrix[0])
    dr, dc = 0, 0

    if direction == 'up':
        dr = -1
    elif direction == 'down':
        dr = 1
    elif direction == 'left':
        dc = -1
    elif direction == 'right':
        dc = 1

    r, c = mouse_pos[0], mouse_pos[1]
    new_r, new_c = r + dr, c + dc

    if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
        return matrix, 'No more cheese for tonight!', mouse_pos

    new_cell = matrix[new_r][new_c]
    if new_cell == '@':
        return matrix, None, mouse_pos

    if new_cell == 'C':
        matrix[new_r][new_c] = '*'
    elif new_cell == 'T':
        return matrix, 'Mouse is trapped!', (new_r, new_c)

    matrix[r][c], matrix[new_r][new_c + 1] = '*', 'M'
    return matrix, None, (new_r, new_c)


N, M = map(int, input().split(','))
cupboard = []
for _ in range(N):
    row = list(input())
    cupboard.append(row)

directions = []
while True:
    direction = input()
    if direction == 'danger':
        break
    directions.append(direction)

mouse_pos, cheese_count, trap_pos = find_mouse(cupboard)

for direction in directions:
    cupboard, message, mouse_pos = move_mouse(cupboard, direction, mouse_pos)

    if message is not None:
        break

if message is None:
    if cheese_count == 0:
        message = 'Mouse will come back later!'
    else:
        message = 'Happy mouse! All the cheese is eaten, good night!'

print(message)
print_matrix(cupboard)
