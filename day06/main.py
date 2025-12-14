with open('./input1.txt', 'r') as f:
    content_of_file = []
    for line in f:
        content_of_file.append(line)


horizontalList = []
for el in content_of_file:
    horizontalList.append(el.split())
operators = horizontalList[-1]
horizontalList.pop(-1)
print(horizontalList)
print(operators)

result = []
for op in operators:
    if op == '+':
        result.append(0)
    else:
        result.append(1)

for lst in horizontalList:
    for i in range(len(operators)):
        if operators[i] == '+':
            result[i] += int(lst[i])
        else:
            result[i] *= int(lst[i])
    # test = combine(horizontalList[0], horizontalList[1], operators)
print(result)

granTotal = 0
for el in result:
    granTotal += el

print(granTotal)
