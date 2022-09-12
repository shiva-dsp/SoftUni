from time import time
from functools import wraps


def measure_time(func):
    def normalize_params(*args, **kwargs):
        params = []
        if args:
            params.append(
                ', '.join(repr(x) for x in args)
            )
        if kwargs:
            params.append(
                ', '.join(f'{key} = {repr(value)}' for key, value in kwargs.items())
            )
        return ', '.join(params)

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        params_string = normalize_params(*args, **kwargs)
        print(f'{func.__name__} ({params_string}) executed in {end_time - start_time}s')
        return result

    return wrapper


@measure_time
def sum_three(x, y, z):
    return x + y + z


print(sum_three(1, 2, 3))
print(sum_three(1, 2, z=3))