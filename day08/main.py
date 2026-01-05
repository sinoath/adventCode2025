junctions = []
with open('./test1.txt') as f:
    for line in f:
        junctions.append(line.strip())

with open('./test1.txt') as f:
    conten_of_file = f.read()


def parse_numbers(s) -> list:
    '''Get a string of 2 number separated by a comma and return a list
    with the three integer as elements'''
    coords = []
    temp = s.split(',')
    for t in temp:
        coords.append(int(t))
    return coords


def get_distance(a, b) -> float:
    '''Calculate the Euclidean distance between two points in 3D space'''
    square = ((b[0] - a[0]) ** 2) + ((b[1] - a[1]) ** 2) + ((b[2] - a[2]) ** 2)
    return square**(1/2)


coordinates = []
for junction in junctions:
    coordinates.append(parse_numbers(junction))

print(coordinates)
