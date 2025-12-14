with open('./test1.txt', 'r') as f:
    content_of_file = []
    for line in f:
        content_of_file.append(line)


print(content_of_file)
horizontalList = []
for el in content_of_file:
    horizontalList.append(el.split())
operators = horizontalList[-1]
print(operators)

def combine(a:list, b:list, ops:list) -> list:
    result = []
    for i in range (len(a)):
        if ops[i] == '*':
            result.append(int(a[i]) * int(b[i]))
        else:
            result.append(int(a[i]) + int(b[i]))
    return result

for i in range(len(operators) -1):
    test = combine(horizontalList[0], horizontalList[1], operators)
print(test)
