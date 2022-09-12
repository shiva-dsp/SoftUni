def fibonacci():
    first = 0
    second = 1
    yield first
    yield second

    while True:
        result = first + second
        first, second = second, result
        yield result



# ------------- tests --------------

generator = fibonacci()
for i in range(5):
    print(next(generator))


generator = fibonacci()
for i in range(1):
    print(next(generator))

# ------------- results ----------------

# 0
# 1
# 1
# 2
# 3

# 0