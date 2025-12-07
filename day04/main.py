f = open('./test1.txt', 'r')
rows = []
for line in f:
    rows.append(line)
f.close()

# Print the matrix
for row in rows:
    print(row, end='')
print()


third_line = rows[2]
print(third_line, end='')
for i in range(len(third_line)):
    if i > 0:
        pass

