def dfs(parent, row, col, matrix, visited):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return
    if visited[row][col]:  # if visited[row][col] == True
        return
    if matrix[row][col] != parent:
        return

    visited[row][col] = True
    dfs(parent, row - 1, col, matrix, visited)
    dfs(parent, row + 1, col, matrix, visited)
    dfs(parent, row, col - 1, matrix, visited)
    dfs(parent, row, col + 1, matrix, visited)


rows = int(input())
cols = int(input())
matrix = []
visited = []

for _ in range(rows):
    matrix.append(list(input()))
    visited.append([False] * cols)

areas = {}
total_areas = 0

for row in range(rows):
    for col in range(cols):
        if visited[row][col]:  # if visited[row][col] == True
            continue
        key = matrix[row][col]
        dfs(key, row, col, matrix, visited)
        if key not in areas:
            areas[key] = 1
        else:
            areas[key] += 1

        total_areas += 1

print(f'Areas: {total_areas}')
for area, size in sorted(areas.items()):
    print(f"Letter '{area}' -> {size}")

# ------------- tests --------------

# 6
# 8
# aacccaac
# baaaaccc
# baabaccc
# bbdaaccc
# ccdccccc
# ccdccccc

# 3
# 3
# aaa
# aaa
# aaa

# 5
# 9
# asssaadas
# adsdasdad
# sdsdadsas
# sdasdsdsa
# ssssasddd

# --------- results ----------

# Areas: 8
# Letter 'a' -> 2
# Letter 'b' -> 2
# Letter 'c' -> 3
# Letter 'd' -> 1

# Areas: 1
# Letter 'a' -> 1

# Areas: 21
# Letter 'a' -> 6
# Letter 'd' -> 7
# Letter 's' -> 8