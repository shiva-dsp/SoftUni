import sys
from io import StringIO
from collections import deque

test_input_1 = '''10 16 13 25
12 11 8
'''

test_input_2 = '''10 14 22 4 5
11 16 17 11 1 8
'''

test_input_3 = '''5 6 7
2 1 5 7 5 3
'''

sys.stdin = StringIO(test_input_1)
# sys.stdin = StringIO(test_input_2)
# sys.stdin = StringIO(test_input_3)

elfs = deque(int(x) for x in input().split(' '))
boxes = [int(x) for x in input().split(' ')]

total_used_energy = 0
total_number_of_toys = 0
counter = 0

while boxes and elfs:
    while elfs and elfs[0] < 5:
        elfs.popleft()

    if not elfs:
        break

    current_box = boxes.pop()
    current_elf = elfs.popleft()

    counter += 1
    created_toys = 1
    spent_energy = current_box
    increase_energy = 1

    if counter % 3 == 0:
        created_toys = 2
        spent_energy *= 2
    if counter % 5 == 0:
        created_toys = 0
        increase_energy = 0

    if current_elf >= spent_energy:
        total_number_of_toys += created_toys
        total_used_energy += spent_energy
        elfs.append(current_elf - spent_energy + increase_energy)
    else:
        boxes.append(current_box)
        elfs.append(current_elf * 2)

print(f'Toys: {total_number_of_toys}')
print(f'Energy: {total_used_energy}')

if elfs:
    print(f'Elves left: {", ".join(str(x) for x in elfs)}')
if boxes:
    print(f'Boxes left: {", ".join(str(x) for x in boxes)}')

# ------------- tests --------------

# 10 16 13 25
# 12 11 8

# 10 14 22 4 5
# 11 16 17 11 1 8

# 5 6 7
# 2 1 5 7 5 3

# --------- results ----------

# Toys: 3
# Energy: 31
# Elves left: 3, 6, 26, 14

# Toys: 7
# Energy: 75
# Elves left: 10, 14

# Toys: 3
# Energy: 20
# Boxes left: 2, 1