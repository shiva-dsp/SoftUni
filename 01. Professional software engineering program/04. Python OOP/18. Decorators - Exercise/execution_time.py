from time import time


def exec_time(func_ref):
    def wrapper(*args):
        start = time()
        result = func_ref(*args)
        end = time()

        with open('./results.txt', 'a') as file:
            file.write(f'{func_ref.__name__} was called with {args}. Elapsed: {end - start}')

        return result

    return wrapper


# ------------- tests --------------

@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 10000000))


# @exec_time
# def concatenate(strings):
#     result = ""
#     for string in strings:
#         result += string
#     return result
#
#
# print(concatenate(["a" for i in range(1000000)]))
#
#
# @exec_time
# def loop():
#     count = 0
#     for i in range(1, 9999999):
#         count += 1
#
#
# print(loop())

# ------------- results --------------

# Note: You might have different results from the given ones.

# 0.8342537879943848

# 0.14537858963012695

# 0.4199554920196533