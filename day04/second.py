f = open('./input1.txt', 'r')
rows = []
for line in f:
    rows.append(line)
f.close()

line_lenght = len(rows[0])
number_of_rows = len(rows)
gran_total_paper_removed = 0
def print_matrix(lines):
    for row in lines:
        print(row, end='')
    print()


def substitute_char_in_matrix(m, char, position):
    '''Get the matrix 'm' (list of lines of characters) and a character, and
    substitute the old character with 'char' in position (couple of integer
    representing the 'line index' and the 'character index' respectively)
    '''
    s = m[position[0]]
    char_pos = el[1]
    s = s[:char_pos] + char + s[char_pos+1:]
    m[el[0]] = s


# print_matrix(rows)

while True:
    line_indexes = []
    movable_paper_coordinates = []
    # Get all index positions of paper rolls '@'
    for row in rows:
        line_indexes.append([i for i in range(line_lenght) if row.startswith('@', i)])


    first = line_indexes[0]
    last = line_indexes[-1]


    # First row case:
    for index in first:
        counter = 0
        positions = [index-1, index+1, index]
        for pos in positions:
            if pos in line_indexes[1]: counter += 1
            if pos in first: counter += 1
        if counter <= 4:
            movable_paper_coordinates.append([0, index])


    # Last row case:
    for index in last:
        counter = 0
        positions = [index-1, index+1, index]
        for pos in positions:
            if pos in line_indexes[-2]: counter += 1
            if pos in last: counter += 1
        if counter <= 4:
            movable_paper_coordinates.append([number_of_rows -1, index])


    # All the other rows
    for i in range(1, len(line_indexes) -1):
        for index in line_indexes[i]:
            counter = 0
            positions = [index-1, index+1, index]
            for pos in positions:
                if pos in line_indexes[i-1]: counter += 1
                if pos in line_indexes[i+1]: counter += 1
                if pos in line_indexes[i]: counter += 1
            if counter <= 4:
                movable_paper_coordinates.append([i, index])



    # print("Total movable paper rolls: ", len(movable_paper_coordinates))
    gran_total_paper_removed += len(movable_paper_coordinates)

    if len(movable_paper_coordinates) == 0:
        break
    else:
        for el in movable_paper_coordinates:
            substitute_char_in_matrix(rows, 'x', el)
        # print_matrix(rows)


        for el in movable_paper_coordinates:
            substitute_char_in_matrix(rows, '.', el)
        # print_matrix(rows)
        line_indexes = []
print(gran_total_paper_removed)
