# def find_all_paths(row, col, matrix, direction, path):
#     if row < 0 or col <0 or row >= len(matrix) or col >= len(matrix[0]):
#         return
#     if matrix[row][col] == 'e':
#         print(''.join(path))
#         path.pop()
#         return
#     if matrix[row][col] == '*':
#         return
#     if matrix[row][col] == 'v':
#         return
#
#     matrix[row][col] = 'v'
#     path.append(direction)
#
#     find_all_paths(row - 1, col, matrix, 'U', path)
#     find_all_paths(row + 1, col, matrix, 'D', path)
#     find_all_paths(row, col - 1, matrix, 'L', path)
#     find_all_paths(row, col + 1, matrix, 'R', path)
#
#     path.pop()
#     matrix[row][col] = '-'
#
#
# rows = int(input())
#
# cols = int(input())
#
# labyrinth = []
#
#
# for _ in range(rows):
#     labyrinth.append(list(input()))
#
# find_all_paths(0, 0, labyrinth, '', [])


def find_all_paths(row, col, matrix, direction, path):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return
    if matrix[row][col] == '*':
        return
    if matrix[row][col] == 'v':
        return

    path.append(direction)

    if matrix[row][col] == 'e':
        print(''.join(path))
    else:
        matrix[row][col] = 'v'

        find_all_paths(row - 1, col, matrix, 'U', path)
        find_all_paths(row + 1, col, matrix, 'D', path)
        find_all_paths(row, col - 1, matrix, 'L', path)
        find_all_paths(row, col + 1, matrix, 'R', path)
        matrix[row][col] = '-'

    path.pop()


rows = int(input())

cols = int(input())

labyrinth = []

for _ in range(rows):
    labyrinth.append(list(input()))

find_all_paths(0, 0, labyrinth, '', [])