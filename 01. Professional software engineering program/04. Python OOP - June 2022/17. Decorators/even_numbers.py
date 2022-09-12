from functools import wraps
from measure_time import measure_time


def even_numbers(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return [x for x in result if x % 2 == 0]

    return wrapper


# ------------- test --------------
@measure_time
@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))

# ------------- result -------------------

# [2, 4]