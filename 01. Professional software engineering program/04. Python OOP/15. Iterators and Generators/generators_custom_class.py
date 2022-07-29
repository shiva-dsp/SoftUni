class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __iter__(self):
        # yield ('name', self.name)
        # yield ('age', self.age)

        for pair in self.__dict__.items():
            yield pair


doncho = Person('Doncho', 19)

for x in doncho:
    print(x)