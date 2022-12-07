#part 1

"""
def getValue(c):
    if  (c == "A" or c =="X"):
        return 1
    elif(c == "B" or c =="Y"):
        return 2
    elif(c == "C" or c =="Z"):
        return 3

def evaluateMove(x, y):
    if (x == y):
        return y + 3
    elif ((x == 1 and y == 3) or (x == 2 and y == 1) or (x == 3 and y == 2)):
        return y
    else:
        return y + 6
  
# 1 = rock
# 2 = paper
# 3 = scissors

input = open('input.txt', 'r')
data = input.readlines()

score = 0

for line in data:
    move = line
    elfMove = getValue(line[0])
    joelMove = getValue(line[2])
    score += evaluateMove(elfMove, joelMove)

print(score)
"""

#part 2

"""
def getValue(c):
    if  (c == "A" or c =="X"):
        return 1
    elif(c == "B" or c =="Y"):
        return 2
    elif(c == "C" or c =="Z"):
        return 3

def getWinningMove(x):
    if (x == 1):
        return 2
    elif (x == 2):
        return 3
    elif (x == 3):
        return 1

def getLosingMove(x):
    if (x == 1):
        return 3
    elif (x == 2):
        return 1
    elif (x == 3):
        return 2

def evaluateMove(x, y):
    if (y == 1):
        return getLosingMove(x) + 0
    elif(y == 2):
        return x + 3
    elif(y == 3):
        return getWinningMove(x) + 6
    

input = open('input.txt', 'r')
data = input.readlines()

score = 0

for line in data:
    move = line
    elfMove = getValue(line[0])
    joelMove = getValue(line[2])
    score += evaluateMove(elfMove, joelMove)

print(score)
"""