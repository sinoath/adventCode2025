file = open('./test1.txt', 'r')
content_of_file = ''
for line in file:
    content_of_file = line[:-1]
file.close()


id_ranges = content_of_file.split(',')

print(id_ranges)
