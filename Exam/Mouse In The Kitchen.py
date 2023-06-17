def move_mouse(matrix, direction, mouse_position):
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
    row, col = mouse_position
    new_row, new_col = row + directions[direction][0], col + directions[direction][1]
    if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
        if matrix[new_row][new_col] == "*":
            matrix[row][col] = "*"
            matrix[new_row][new_col] = "M"
            return (new_row, new_col)
        elif matrix[new_row][new_col] == "C":
            matrix[row][col] = "*"
            matrix[new_row][new_col] = "M"
            if count_cheese(matrix) == 0:
                return "all_eaten"
            else:
                return (new_row, new_col)
        elif matrix[new_row][new_col] == "T":
            matrix[row][col] = "*"
            matrix[new_row][new_col] = "M"
            return "trapped"
    return mouse_position


def count_cheese(matrix):
    count = 0
    for row in matrix:
        count += row.count("C")
    return count


def print_matrix(matrix):
    for row in matrix:
        print("".join(row))


dimensions = input().split(",")
rows, cols = int(dimensions[0]), int(dimensions[1])

cupboard = []
mouse_position = None

for _ in range(rows):
    row = list(input())
    cupboard.append(row)
    if "M" in row:
        mouse_position = (len(cupboard) - 1, row.index("M"))

directions = []
while True:
    direction = input()
    if direction == "danger":
        print("Mouse will come back later!")
        break
    directions.append(direction)

    mouse_position = move_mouse(cupboard, direction, mouse_position)
    if mouse_position == "trapped":
        print("Mouse is trapped!")
        break
    elif mouse_position == "all_eaten":
        print("Happy mouse! All the cheese is eaten, good night!")
        break

    cheese_count = count_cheese(cupboard)
    if cheese_count == 0:
        print("Happy mouse! All the cheese is eaten, good night!")
        break
    elif cheese_count > 0 and not directions:
        print("Mouse will come back later!")
        break

print_matrix(cupboard)
