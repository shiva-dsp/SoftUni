def squares(n):

    # for x in range(1, n + 1):
    #     yield x * x

    value = 1
    while value < n + 1:
        yield value * value
        value += 1

print(*squares(5))