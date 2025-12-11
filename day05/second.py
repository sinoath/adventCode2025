from typing import Optional


f = open('./input1.txt', 'r')
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
unique_IDs_quantity = 0

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


def mySortKey(l):
    return l[0]


ranges_fresh_food.sort(key=mySortKey)
print(ranges_fresh_food)
optmized_ranges = []
optmized_ranges.append(ranges_fresh_food[0])


for i in range(1, len(ranges_fresh_food)):
    if ranges_fresh_food[i][1] <= optmized_ranges[i-1][1]:
        optmized_ranges.insert(0, [0, 0])
    elif ranges_fresh_food[i][0] > optmized_ranges[i-1][1]:
        optmized_ranges.append(ranges_fresh_food[i])
    else:
        temp = [optmized_ranges[i-1][0], ranges_fresh_food[i][1]]
        optmized_ranges.insert(0, [0, 0])
        optmized_ranges.pop(-1)
        optmized_ranges.append(temp)
    print(optmized_ranges)

while [0, 0] in optmized_ranges:
    optmized_ranges.remove([0, 0])

for el in optmized_ranges:
    temp = el[1] - el[0] +1
    unique_IDs_quantity += temp


print(unique_IDs_quantity)
