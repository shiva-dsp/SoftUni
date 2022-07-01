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


def print_rhombus(n):
    for i in range(n):
        spaces_count = n - 1 - i
        stars_count = i + 1
        print(' ' * spaces_count + '* ' * stars_count)
    for i in range(n - 2, -1, -1):
        spaces_count = n - 1 - i
        stars_count = i + 1
        print(' ' * spaces_count + '* ' * stars_count)



print_rhombus(3)
print_rhombus(4)