from collections import deque

sequence_of_seats = input().split(', ')

first = deque(int(x) for x in input().split(', '))
second = deque(int(x) for x in input().split(', '))

rotations_count = 0
matches_counter = 0

seat_matches = []

while sequence_of_seats:

    if rotations_count == 10:
        break

    rotations_count += 1

    current_first = first.popleft()
    current_second = second.pop()

    total_sum = current_first + current_second
    current_ascii = chr(total_sum)

    seat_1 = str(current_first) + current_ascii
    seat_2 = str(current_second) + current_ascii

    if seat_1 in sequence_of_seats or seat_2 in sequence_of_seats:
        if seat_1 in sequence_of_seats:
            seat_matches.append(seat_1)
            matches_counter += 1
            sequence_of_seats.remove(seat_1)
        if matches_counter == 3:
            break

        if seat_2 in sequence_of_seats:
            seat_matches.append(seat_2)
            matches_counter += 1
            sequence_of_seats.remove(seat_2)
        if matches_counter == 3:
            break

    else:
        first.append(current_first)
        second.appendleft(current_second)

print(f"Seat matches: {', '.join(seat_matches)}")
print(f"Rotations count: {rotations_count}")

# ------------- tests --------------

# 17K, 20B, 3C, 15D, 31Z, 28F
# 20, 35, 15, 3, 2, 10
# 1, 15, 64, 53, 45, 46

# 25A, 16B, 44T, 49D, 27M, 44F
# 25, 3, 31, 49, 26, 13
# 10, 15, 44, 40

# 15C, 25C, 36C, 43P, 40E, 38G
# 15, 25, 80, 40, 15, 99, 52
# 15, 42, 29

# --------- results ----------

# Seat matches: 20B, 15D, 3C
# Rotations count: 4

# Seat matches: 25A, 44F
# Rotations count: 10

# Seat matches: 25C, 40E, 15C
# Rotations count: 7