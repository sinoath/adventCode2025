f = open('./input1.txt', 'r')
rows = []
for line in f:
    rows.append(line)
f.close()

quantity_of_digits = 12
from_left = 0
max_per_line_joltage = []
first_digit_pos = 0
second_digit_pos = 0
total_joltage = 0


def position_max_left_digit(s:str, start=0, end=-1):
    '''Find the position of the leftmost greater number in a given string
    Input: s: string, start: int, end: int
    Output: postion: int
    '''
    for i in range(9, -1, -1):
        position = s.find(str(i), start, end)
        if position != -1:
            return position
    return -1


digit_position = 0
for row in rows:
    found = ''
    for i in range(-quantity_of_digits, 1, 1):
        digit_pos = position_max_left_digit(row, from_left, i)
        found += row[digit_pos]
        from_left = digit_pos + 1
    max_per_line_joltage.append(found)


for el in max_per_line_joltage:
    total_joltage += int(el)


print('total: ', total_joltage)
