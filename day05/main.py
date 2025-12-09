f = open('./test1.txt', 'r')
content_of_file = []
for line in f:
    content_of_file.append(line)
f.close()

blankline = content_of_file.index("\n")
first_half = content_of_file[:blankline]
second_half = content_of_file[blankline+1:]
foodIDs = []
ranges_fresh_food = []
freshy = 0
unique_IDs = set()

for id in second_half:
    id = int(id[:-1])
    foodIDs.append(id)


# print(foodIDs)


for el in first_half:
    temp = []
    el = el[:-1]
    temp = el.split('-')
    ranges_fresh_food.append([int(temp[0]), int(temp[1])])
# print(ranges_fresh_food)

for food in foodIDs:
    for spread in ranges_fresh_food:
        if spread[0] <= food and food <= spread[1]:
            freshy += 1
            break

print(freshy)
