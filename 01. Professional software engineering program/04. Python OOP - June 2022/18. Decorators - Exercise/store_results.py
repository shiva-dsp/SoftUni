# def store_results(func_ref):
#     def wrapper(*args):
#         result = func_ref(*args)
#
#         with open('./results.txt', 'a') as file:
#             file.write(f"Function '{func_ref.__name__}' was called. Result: {result}")
#             file.write('\n')
#
#         return result
#
#     return wrapper

class store_results:
    def __init__(self, func_ref):
        self.func_ref = func_ref

    def __call__(self, *args, **kwargs):
        result = self.func_ref(*args)

        with open('./results.txt', 'a') as file:
            file.write(f"Function '{self.func_ref.__name__}' was called. Result: {result}")
            file.write('\n')

        return result


# ------------- tests --------------

@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)

# ------------- results -------------------

# Function 'add' was called. Result: 4


# Function 'mult' was called. Result: 24