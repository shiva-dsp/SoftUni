def number_increment(numbers):

    def increase():
        return [x + 1 for x in numbers]

    return increase()

# ------------- test --------------

print(number_increment([1, 2, 3]))

# ------------- results ----------------

# [2, 3, 4]