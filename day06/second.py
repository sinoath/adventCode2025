with open('./input1.txt', 'r') as f:
    content_of_file = []
    for line in f:
        content_of_file.append(line)


horizontalList = []
for el in content_of_file:
    horizontalList.append(el[:-1])
operators = horizontalList[-1]
horizontalList.pop(-1)
op_positions = []

for i in range(len(operators)):
    if not operators[i].isspace():
        op_positions.append(i)

parsedCol = ['' for _ in range(len(operators))]
firstLine = horizontalList[0]

for el in horizontalList:
    for i in range(len(firstLine)):
        parsedCol[i] += el[i]

for i in range(len(parsedCol)):
    parsedCol[i] = parsedCol[i].strip()

columns = [[op, []] for op in operators if not op.isspace()]

j = 0
for idx in range(len(parsedCol)):
    if parsedCol[idx] == '':
        j += 1
        continue
    columns[j][1].append(parsedCol[idx])

totals = []
for el in columns:
    if el[0] == '+':
        result = 0
        for add in el[1]:
            result += int(add)
        totals.append(result)
    else:
        result = 1
        for mul in el[1]:
            result *= int(mul)
        totals.append(result)

granTotal = 0
for el in totals:
    granTotal += el
print(granTotal)
