ROWS = 6
COLUMNS = 6

matrix = [input().split(' ') for _ in range(ROWS)]

start_position = input()

row = int(start_position[1])
column = int(start_position[4])

while True:
    input_data = input().split(', ')

    command = input_data[0]

    if command == 'Stop':
        break

    direction = input_data[1]

    if command == 'Create':
        value = input_data[2]
        if direction == 'up':
            row -= 1
        elif direction == 'down':
            row += 1
        elif direction == 'left':
            column -= 1
        elif direction == 'right':
            column += 1
        if matrix[row][column] == '.':
            matrix[row][column] = value

    elif command == 'Update':
        value = input_data[2]
        if direction == 'up':
            row -= 1
        elif direction == 'down':
            row += 1
        elif direction == 'left':
            column -= 1
        elif direction == 'right':
            column += 1
        if matrix[row][column] != '.':
            matrix[row][column] = value

    elif command == 'Delete':
        if direction == 'up':
            row -= 1
        elif direction == 'down':
            row += 1
        elif direction == 'left':
            column -= 1
        elif direction == 'right':
            column += 1
        if matrix[row][column] != '.':
            matrix[row][column] = '.'

    elif command == 'Read':
        if direction == 'up':
            row -= 1
        elif direction == 'down':
            row += 1
        elif direction == 'left':
            column -= 1
        elif direction == 'right':
            column += 1
        if matrix[row][column] != '.':
            print(matrix[row][column])

for row in matrix:
    print(' '.join(row))

# ------------- tests --------------

# . . . . . .
# . 6 . . . .
# G . S . t S
# . . 10 . . .
# . 95 . . 8 .
# . . P . . .
# (1, 1)
# Create, down, r
# Update, right, e
# Create, right, a
# Read, right
# Delete, right
# Stop


# . . . . . .
# . 6 . . . .
# . T . D . O
# . . 10 A . .
# . 95 . 80 5 .
# . . P . t .
# (2, 3)
# Create, down, o
# Delete, right
# Read, up
# Create, left, 20
# Update, up, P
# Stop


# H 8 . . . .
# 70 i . . . .
# t . . . B .
# 50 . 16 . C .
# . . . t . .
# . 25 . . . .
# (0, 0)
# Read, right
# Read, down
# Read, left
# Delete, down
# Create, right, 10
# Read, left
# Stop

# --------- results ----------

# t
# . . . . . .
# . 6 . . . .
# G r e a t .
# . . 10 . . .
# . 95 . . 8 .
# . . P . . .


# . . . . . .
# . 6 . . . .
# . T . D . O
# . . 10 A . .
# . 95 . 80 5 .
# . . P . t .


# 8
# i
# 70
# H 8 . . . .
# 70 i . . . .
# . 10 . . B .
# 50 . 16 . C .
# . . . t . .
# . 25 . . . .