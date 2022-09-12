from itertools import permutations


def possible_permutations(data: list):
    for result in permutations(data):
        yield list(result)


# ------------- tests --------------

[print(n) for n in possible_permutations([1, 2, 3])]

[print(n) for n in possible_permutations([1])]

# ------------- results --------------

# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]

# [1]