# from functools import wraps


def multiply(times):
    def decorator(function):
        # @wraps(times)
        def wrapper(*args, **kwargs):
            return times * function(*args, **kwargs)

        return wrapper

    return decorator


# ------------- tests --------------

@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))


@multiply(5)
def add_ten(number):
    return number + 10


print(add_ten(6))

# ------------- results -------------------

# 39 ... comment: First, we add 3 to 10 = 13,
#                 and then we multiply the result by 3: 13 * 3 = 39

# 80 ... comment: (6 + 10) * 5 = 80