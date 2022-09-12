def count_all_path(row, col, rows, cols):
    if row >= rows or col >= cols:
        return 0
    if row == rows - 1 and col == cols - 1:
        return 1

    result = 0
    result += count_all_path(row, col + 1, rows, cols)  # Right
    result += count_all_path(row + 1, col, rows, cols)  # Down

    return result


rows = int(input())
cols = int(input())

print(count_all_path(0, 0, rows, cols))

# --------- tests ----------

# 3
# 2

# 3
# 5

#  --------- results ----------

# 3

# 15