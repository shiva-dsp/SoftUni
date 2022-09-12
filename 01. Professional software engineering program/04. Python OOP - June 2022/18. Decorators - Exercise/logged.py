def logged(func_ref):
    def wrapper(*args):
        result = func_ref(*args)
        return f'you called {func_ref.__name__}{args}\nit returned {result}'

    return wrapper



# ------------- tests --------------

@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))

# ------------- results --------------

# you called func(4, 4, 4)
# it returned 6


# you called sum_func(1, 4)
# it returned 5