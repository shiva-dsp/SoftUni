def calc_binom(n, k, memo):
    key = f'{n} {k}'
    if key in memo:
        return memo[key]
    if n == 0 or k == 0 or n == k:
        return 1

    result = calc_binom(n - 1, k - 1, memo) + calc_binom(n - 1, k, memo)
    memo[key] = result
    return result


n = int(input())
k = int(input())

print(calc_binom(n, k, {}))

# ------------- tests --------------

# 3
# 2

# 4
# 0

# 6
# 2

# 49
# 10

# --------- results ----------

# 3

# 1

# 15

# 8217822536