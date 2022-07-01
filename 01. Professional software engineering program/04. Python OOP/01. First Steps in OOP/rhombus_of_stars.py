'''
n = 3
  *      # i = 0, 2 spaces (n - 1 - i spaces), 1 star
 * *     # i = 1, 1 spaces (n - 1 - i spaces), 1 star, 1 space, 1 star
* * *    # i = 2, 0 spaces, 1 star, 1 space, 1 star, 1 space, 1 star
 * *
  *


n = 4
   *
  * *
 * * *
* * * *
 * * *
  * *
   *

'''


# def get_line(i, n):
#     spaces_count = n - 1 - i
#     stars_count = i + 1
#     return ' ' * spaces_count + ('* ' * stars_count).strip()
#
#
# def print_rhombus(n):
#     for i in range(n):
#         print(get_line(i, n))
#     for i in range(n - 2, -1, -1):
#         print(get_line(i, n))


def get_line(i, n):
    spaces_count = n - 1 - i
    stars_count = i + 1
    return ' ' * spaces_count + ('* ' * stars_count).strip()


def get_rhombus(n):
    return [get_line(i, n) for i in range(n)] + \
           [get_line(i, n) for i in range(n - 2, -1, -1)]


def print_line(n):
    print(get_line(n - 1, n - 1))


def print_square(n):
    [print(get_line(n - 1, n - 1)) for _ in range(n)]


def print_rhombus(n):
    for i in range(n):
        print(get_line(i, n))
    for i in range(n - 2, -1, -1):
        print(get_line(i, n))


print_rhombus(3)
print_rhombus(4)
print_square(5)