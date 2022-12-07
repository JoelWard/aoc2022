#part 1
"""
input = open('input.txt', 'r')
data = input.readlines()

score = 0
points = 0

for line in data:
    items = line
    size = int((len(items)-1)/2)
    sack1 = items[0:size]
    sack2 = items[size:size*2]
    print(sack1, sack2)
    print(line)

    for x in range(size):
        if sack1[x] in sack2:
            found = sack1[x]

    if found.isupper():
        points = ord(found.lower()) - ord('a') + 1 + 26
    else:
        points = ord(found) - ord('a') + 1

    score += points
        

print(score)
"""

#part 2
import linecache
score = 0
n = 1

for x in range(100):
    sack1 = linecache.getline('input.txt', n)
    sack2 = linecache.getline('input.txt', n + 1)
    sack3 = linecache.getline('input.txt', n + 2)

    for x in range(len(sack1) - 1):
        if sack1[x] in sack2 and sack1[x] in sack3:
            found = sack1[x]

    for x in range(len(sack2) - 1):
        if sack2[x] in sack1 and sack2[x] in sack3:
            found = sack2[x]

    for x in range(len(sack3) - 1):
        if sack3[x] in sack1 and sack3[x] in sack2:
            found = sack3[x]

    if found.isupper():
        points = ord(found.lower()) - ord('a') + 1 + 26
    else:
        points = ord(found) - ord('a') + 1

    score += points

    n += 3

print(score)