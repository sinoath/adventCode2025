with open('./test1.txt', 'r') as f:
    content_of_file = []
    for line in f:
        content_of_file.append(line)


horizontalList = []
for el in content_of_file:
    horizontalList.append(el[:-1])
operators = horizontalList[-1]
horizontalList.pop(-1)
# print(horizontalList)
# print(operators)
op_positions = []
for i in range(len(operators)):
    if not operators[i].isspace():
        op_positions.append(i)
print(op_positions)
testList = ['' for _ in range(len(operators))]
# print(len(testList))
# print(len(operators))
# print(operators)
# print(testList)
firstLine = horizontalList[0]
for el in horizontalList:
    for i in range(len(firstLine)):
        testList[i] += el[i]
# print(testList)
# print(testList[-1].strip() + '. ')
 
for pos in op_positions:
    if pos == op_positions[-1]:
        pass
    else:
        pass
