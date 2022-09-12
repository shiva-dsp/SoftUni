class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'"{self.name}" by {self.author} has {self.pages}'


# b = Book('Harry Potter and GoF', 'J.K.Rowling', 500)
#
# print(b)
# print(str(b))
# print(b.name)
# print(b.author)
# print(b.pages)

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f'{self.name} is the best animal ...'
#
#     def sleep(self):
#         return "sleeping .."
#
# animal = Animal("cat")
# print(animal.sleep())
# print(animal.name)
# print(animal)