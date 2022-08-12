from collections import deque

first = input().split()
second = input().split()

rows = len(first) + 1
cols = len(second) + 1

dp = []
[dp.append([0] * cols) for _ in range(rows)]

for row in range(1, rows):
    for col in range(1, cols):
        if first[row - 1] == second[col - 1]:
            dp[row][col] = dp[row - 1][col - 1] + 1
        else:
            dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

row = rows - 1
col = cols - 1
result = deque()

while row > 0 and col > 0:
    if first[row - 1] == second[col - 1]:
        result.appendleft(first[row - 1])
        row -= 1
        col -= 1

    elif dp[row - 1][col] > dp[row][col - 1]:
        row -= 1
    else:
        col -= 1

print(' '.join(result))
print(len(result))

# ------------- tests --------------

# 13 42 69 73 42 84 26
# 13 54 73 42 8 15 29

# 5 69 78 5 3 5 5 5
# 1 2 3 5 5 5 5 5

# --------- results ----------

# 13 73 42
# 3

# 5 5 5 5 5
# 5