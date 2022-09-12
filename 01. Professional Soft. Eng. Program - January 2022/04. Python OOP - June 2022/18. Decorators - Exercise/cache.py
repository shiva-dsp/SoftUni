def cache(func_ref):
    memo = {}

    def wrapper(n):
        if n in memo:
            return memo[n]
        result = func_ref(n)
        memo[n] = result
        return result

    wrapper.log = memo
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# ------------- tests --------------

fibonacci(3)
print(fibonacci.log)

fibonacci(4)
print(fibonacci.log)

# ------------- results --------------

# {1: 1, 0: 0, 2: 1, 3: 2}

# {1: 1, 0: 0, 2: 1, 3: 2, 4: 3}