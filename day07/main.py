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
    Input: str, str, list[int]
    Output: str
    '''
    if i < len(s):
        s = s[:i] + c + s[i+1:]
    return s


rows[0] = rows[0].replace("S", "|")
beam_x = rows[0].find('|')
# rows[1] = rows[1][:beam_x] + '|' + rows[1][beam_x+1:]
rows[1] = char_replace('|', rows[1], beam_x)
splitter_coords = []


print()
print(rows[0])
print(rows[1])


for line_id in range(len(rows)):
    if '^' in rows[line_id]:
        splitter_coords.append([line_id, []])


for coord in splitter_coords:
    line = rows[coord[0]]
    for c in range(len(line)):
        if line[c] == '^':
            coord[1].append(c)


print(splitter_coords)

