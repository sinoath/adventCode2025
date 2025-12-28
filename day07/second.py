with open('./test1.txt') as f:
    content_of_file = f.read()

print(content_of_file)

rows = []
with open('./test1.txt') as f:
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


deviation_beam = 0


timelines = []
for l in range(1, len(rows)):
    if l % 2 != 0:
        for el in beam_x:
            rows[l] = char_replace('|', rows[l], el)
    else:
        temp = set()
        for i in range(len(rows[l])):
            if rows[l][i] == '^' and i in beam_x:
                deviation_beam += 1
                beam_x.remove(i)
                temp.add(i-1)
                temp.add(i+1)
        for t in temp:
            beam_x.add(t)
        for el in beam_x:
            rows[l] = char_replace('|', rows[l], el)

for el in rows:
    print(el)
print(deviation_beam)
