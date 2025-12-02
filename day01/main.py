f = open('./input1.txt', 'r')
rows = []
for line in f:
    rows.append((line[0], line[1:-1]))
f.close()
# print(rows)
counter = 0
starting_point = 50


def rotation(position, direction, steps):
    if len(steps) > 2:
        st = int(steps[-2:])
    else:
        st = int(steps)

    if direction == 'R':
        temp = position + st
    else:
        temp = 100 - st + position
    return temp % 100

for row in rows:
    starting_point = rotation(starting_point, row[0], row[1])
    if starting_point == 0:
        counter += 1
    # print(starting_point)
print("Number of zeroes: ", counter)
