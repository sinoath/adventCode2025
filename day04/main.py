f = open('./input1.txt', 'r')
rows = []
for line in f:
    rows.append(line)
f.close()

line_indexes = []
line_lenght = len(rows[0])
movable_paper_coordinates = []
number_of_rows = len(rows)
# Print the matrix and get all index positions of paper rolls '@'
for row in rows:
    line_indexes.append([i for i in range(line_lenght) if row.startswith('@', i)])
    print(row, end='')
print()

first = line_indexes[0]
last = line_indexes[-1]


# First row case:
for index in first:
    counter = 0
    positions = [index-1, index+1, index]
    for pos in positions:
        if pos in line_indexes[1]: counter += 1
    for pos in positions[:-1]: 
        if pos in first: counter += 1
    if counter <= 3:
        movable_paper_coordinates.append([0, index])


# Last row case:
for index in last:
    counter = 0
    positions = [index-1, index+1, index]
    for pos in positions:
        if pos in line_indexes[-2]: counter += 1
    for pos in positions[:-1]: 
        if pos in last: counter += 1
    if counter <= 3:
        movable_paper_coordinates.append([number_of_rows -1, index])


# All the other rows
for i in range(1, len(line_indexes) -1):
    for index in line_indexes[i]:
        counter = 0
        positions = [index-1, index+1, index]
        for pos in positions:
            if pos in line_indexes[i-1]: counter += 1
        for pos in positions:
            if pos in line_indexes[i+1]: counter += 1
        if counter > 3:
            continue
        for pos in positions[:-1]:
            if pos in line_indexes[i]: counter += 1
        if counter <= 3:
            movable_paper_coordinates.append([i, index])



for index in line_indexes:
    print(index)


for el in movable_paper_coordinates:
    print(el)
# print('\n', first, '\n', last)
print("Total movable paper rolls: ", len(movable_paper_coordinates))
