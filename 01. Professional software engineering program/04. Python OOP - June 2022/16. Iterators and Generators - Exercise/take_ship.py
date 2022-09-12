class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.iterations = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations == self.count:
            raise StopIteration
        result = self.iterations * self.step
        self.iterations += 1
        return result



# ------------- test code -----------

numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)

# ------------- outputs --------------------

# 0
# 2
# 4
# 6
# 8
# 10


# 0
# 10
# 20
# 30
# 40