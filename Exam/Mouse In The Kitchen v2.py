def is_valid_move(matrix, row, col):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])


def find_initial_position(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 'M':
                return row, col


def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))


def cheese_hunt():
    rows, cols = map(int, input().split(','))
    matrix = [list(input()) for _ in range(rows)]
    directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    traps = []
    cheeses = 0

    # Find initial mouse position and count traps and cheeses
    mouse_row, mouse_col = find_initial_position(matrix)
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 'T':
                traps.append((row, col))
            elif matrix[row][col] == 'C':
                cheeses += 1

    while True:
        command = input().strip()
        if command == 'danger':
            print("Mouse will come back later!")
            break

        # Calculate new position based on the command
        move_row, move_col = directions[command]
        new_row, new_col = mouse_row + move_row, mouse_col + move_col

        # Check if the new position is valid
        if is_valid_move(matrix, new_row, new_col):
            if matrix[new_row][new_col] == 'C':
                cheeses -= 1
                matrix[new_row][new_col] = '*'
                if cheeses == 0:
                    print("Happy mouse! All the cheese is eaten, good night!")
                    print_matrix(matrix)
                    return
            elif matrix[new_row][new_col] == 'T':
                matrix[mouse_row][mouse_col] = '*'
                print("Mouse is trapped!")
                print_matrix(matrix)
                return
            elif matrix[new_row][new_col] == '@':
                continue

            matrix[mouse_row][mouse_col] = '*'
            matrix[new_row][new_col] = 'M'
            mouse_row, mouse_col = new_row, new_col
        else:
            print("No more cheese for tonight!")
            print_matrix(matrix)
            return


cheese_hunt()
