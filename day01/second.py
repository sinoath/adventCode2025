f = open('./input1.txt', 'r')
rows = []
for line in f:
    rows.append((line[0], line[1:-1]))
f.close()
counter = 0
starting_point = 50


def rotationL(position, steps):
    global counter
    st = int(steps[-2:])
    if (position - st) <= 0 and position != 0:
        counter += 1
    if len(steps) > 2:
        counter += int(steps[0:-2])
    return (100 + position - st) % 100


def rotationR(position, steps):
    global counter
    st = int(steps[-2:])
    if (position + st) >= 100:
        counter += 1
    if len(steps) > 2:
        counter += int(steps[0:-2])
    return (position + st) % 100


for row in rows:
    direct = row[0]
    moves = row[1]
    if direct.capitalize() == 'R':
        starting_point = rotationR(starting_point, moves)
    else:
        starting_point = rotationL(starting_point, moves)
print("Number of zeroes: ", counter)
