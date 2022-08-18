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