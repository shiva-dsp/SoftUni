def tags(tag: str):
    def decorator(func_ref):
        def wrapper(*args):
            result = func_ref(*args)
            return f'<{tag}>{result}</{tag}>'

        return wrapper

    return decorator


# ------------- tests --------------

@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))

# ------------- results --------------

# <p>Hello you!</p>

# <h1>HELLO</h1>