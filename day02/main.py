file = open('./test1.txt', 'r')
content_of_file = ''
for line in file:
    content_of_file = line[:-1]
file.close()


def match_split(id:str):
    '''Check if the first half of a string is equal to the second half'''
    half = len(id) / 2
    first_half = id[:half]
    second_half = id[half:]
    return first_half == second_half


# Variables
id_ranges = content_of_file.split(',')
maybe_faulty_ids = []
faulty_ids = []
sum_ids = 0

print(id_ranges)
