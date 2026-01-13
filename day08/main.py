junctions = []
with open('./test1.txt') as f:
    for line in f:
        junctions.append(line.strip())


def parse_numbers(s) -> tuple:
    '''Get a string of 2 number separated by a comma and return a tuple
    with the three integer as coordinates'''
    coords = []
    temp = s.split(',')
    for t in temp:
        coords.append(int(t))
    return tuple(coords)


def get_distance(a, b) -> float:
    '''Calculate the Euclidean distance between two points in 3D space'''
    square = ((b[0] - a[0]) ** 2) + ((b[1] - a[1]) ** 2) + ((b[2] - a[2]) ** 2)
    return square**(1/2)


def closest_distance(coord, all_coords:list) -> tuple:
    '''Input a junction's coordinates "coord" and all the other coordinates,
    output the closest (to coords) junctions's coordinates'''
    temp = [x for x in all_coords]
    if coord in temp:
        temp.remove(coord)
    closest = temp[0]
    min_distance = get_distance(coord, closest)
    for t in temp:
        distance = get_distance(coord, t)
        if distance < min_distance and distance > 0:
            min_distance = distance
            closest = t
    return (coord, closest, min_distance)


def my_key_func(t:tuple):
    return t[2]


coordinates = []
for junction in junctions:
    coordinates.append(parse_numbers(junction))


pairs_closest = []
for coord in coordinates:
    clst = closest_distance(coord, coordinates)
    if (clst[1], clst[0], clst[2]) not in pairs_closest:
        pairs_closest.append(clst)

