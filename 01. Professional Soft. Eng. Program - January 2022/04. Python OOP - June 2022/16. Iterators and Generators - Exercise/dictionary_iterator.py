# class dictionary_iter:
#     def __init__(self, data: dict):
#         self.items = list(data.items())
#         self.idx = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.idx >= len(self.items):
#             raise StopIteration()
#
#         result = self.items[self.idx]
#         self.idx += 1
#         return result

# ------------- var_2 --------------

class dictionary_iter:
    def __init__(self, data: dict):
        self.data = data
        self.genetator = (pair for pair in self.data.items())

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.genetator)


# -------------tests --------------

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)

# ------------- results --------------------

# (1, '1')
# (2, '2')

# ("name", "Peter")
# ("age", 24)