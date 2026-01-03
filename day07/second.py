with open('./input1.txt') as f:
    content_of_file = f.read()

print(content_of_file)

rows = []
with open('./input1.txt') as f:
    for line in f:
        rows.append(line.rstrip())


def char_replace(c:str, s:str, i:int) -> str:
    '''Change the character in string "s" with index "i"
    with the character "c"
    Input: string, string, integer
    Output: string
    '''
    if i < len(s):
        s = s[:i] + c + s[i+1:]
    return s


rows[0] = rows[0].replace("S", "|")
beam_x = {rows[0].find('|')}
splitter_coords = []


for line_id in range(len(rows)):
    if '^' in rows[line_id]:
        splitter_coords.append([line_id, []])


for coord in splitter_coords:
    line = rows[coord[0]]
    for c in range(len(line)):
        if line[c] == '^':
            coord[1].append(c)


deviation_beam = [ 1 if i in beam_x else 0 for i in range(len(rows[0]))]


for line_num in range(1, len(rows)):
    if line_num % 2 != 0:
        for ray in beam_x:
            rows[line_num] = char_replace('|', rows[line_num], ray)
    else:
        temp = set()
        for cell in range(len(rows[line_num])):
            if rows[line_num][cell] == '^' and cell in beam_x:
                beam_x.remove(cell)
                temp.add(cell-1)
                deviation_beam[cell-1] += deviation_beam[cell]
                temp.add(cell+1)
                deviation_beam[cell+1] += deviation_beam[cell]
                deviation_beam[cell] = 0
        for t in temp:
            beam_x.add(t)
        for ray in beam_x:
            rows[line_num] = char_replace('|', rows[line_num], ray)


total = 0
for x in deviation_beam:
    total += x

print(total)
