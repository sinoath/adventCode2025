with open('./test1.txt', 'r') as f:
    content_of_file = []
    for line in f:
        content_of_file.append(line)


horizontalList = []
for el in content_of_file:
    horizontalList.append(el[:-1])
operators = horizontalList[-1]
horizontalList.pop(-1)
print(horizontalList)
print(operators)
