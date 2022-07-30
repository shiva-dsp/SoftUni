from time import time
from functools import wraps


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'{func.__name__} executed in {end - start}')
        return result

    return wrapper


@measure_time
def sum_three(x, y, z):
    return x + y + z


print(sum_three(1, 2, 3))
print(sum_three(1, 2, z=3))