#part 1
"""
input = open('input.txt', 'r')
data = input.readlines()

score = 0

for line in data:
    pair1 = line.partition(",")[0]
    pair2 = line.partition(",")[2]
    
    min1 = int(pair1.partition("-")[0])
    max1 = int(pair1.partition("-")[2])

    min2 = int(pair2.partition("-")[0])
    max2 = int(pair2.partition("-")[2])

    if (min1 <= min2 and max1 >= max2):
        score+=1
    elif (min1 >= min2 and max1 <= max2):
        score+=1

print(score)
"""

#part 2

input = open('input.txt', 'r')
data = input.readlines()

score = 0

for line in data:
    pair1 = line.partition(",")[0]
    pair2 = line.partition(",")[2]
    
    min1 = int(pair1.partition("-")[0])
    max1 = int(pair1.partition("-")[2])

    min2 = int(pair2.partition("-")[0])
    max2 = int(pair2.partition("-")[2])

    if (max1 >= min2 and max2 >= min1):
            score += 1

print(score)