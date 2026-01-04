junctions = []
with open('./test1.txt') as f:
    for line in f:
        junctions.append(line.strip())

with open('./test1.txt') as f:
    conten_of_file = f.read()

# print(conten_of_file)
# print(junctions)
# print(junctions[0].split(','))

temp = []
for t in junctions[0].split(','):
    temp.append(int(t))

print(temp)


def parse_numbers(s) -> list:
    coords = []
    temp = s.split(',')
    print(temp)
    for t in temp:
        coords.append(int(t))
    return coords


def get_distance(a, b) -> float:
    return a / b


print(parse_numbers(junctions[0]))
