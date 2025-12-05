file = open('./input1.txt', 'r')
# file = open('./test1.txt', 'r')
content_of_file = ''
for line in file:
    content_of_file = line[:-1]
file.close()


# Variables
id_ranges = content_of_file.split(',')
maybe_faulty_ids = []
faulty_ids = []
sum_ids = 0


def match_split(id:str):
    '''Check if a string is a repeated pattern of any number of chars
    Input: str
    Output: bool
    '''
    lenght = len(id)
    quotient = 2
    while lenght >= quotient:
        if lenght % quotient == 0:
            slice = lenght // quotient
            pattern = id[:slice]
            if id.count(pattern) == quotient:
                return True
        quotient += 1
    return False


# Splitting the begin and end of the range
for id_range in id_ranges:
    temp = id_range.split('-')
    maybe_faulty_ids.append(temp)


for id in maybe_faulty_ids:
    start = int(id[0])
    end = int(id[1])
    for i in range (start, end + 1):
        if match_split(str(i)):
            faulty_ids.append(str(i))
            sum_ids += i


print(f"Sum of faulty IDs: {sum_ids}")
