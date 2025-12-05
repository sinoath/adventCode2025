f = open('./input1.txt', 'r')
rows = []
for line in f:
    rows.append(line[:-1])
f.close()

# print(rows)
quantity_of_digits = 12
from_left = 0
max_line_joltage = []
first_digit_pos = 0
second_digit_pos = 0
total_joltage = 0


def position_max_left_digit(s:str):
    for i in range(9, -1, -1):
        position = s.find(str(i), 0, -1)
        if position != -1:
            return position
    return -1


def position_max_right_digit(s:str, index:int):
    for i in range(9, -1, -1):
        position = s.find(str(i), index)
        if position != -1:
            return position
    return -1


for row in rows:
    first_digit_pos = position_max_left_digit(row)
    from_left = first_digit_pos + 1
    second_digit_pos = position_max_right_digit(row, from_left)
    max_line_joltage.append(row[first_digit_pos]+row[second_digit_pos])
    # print(row, row[first_digit_pos]+row[second_digit_pos])


for el in max_line_joltage:
    total_joltage += int(el)


print("Total joltage: ", total_joltage)
