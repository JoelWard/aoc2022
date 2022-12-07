#part 1

stack1 = ["B", "P", "N", "Q", "H", "D", "R", "T"]
stack2 = ["W", "G", "B", "J", "T", "V"]
stack3 = ["N", "R", "H", "D", "S", "V", "M", "Q"]
stack4 = ["P", "Z", "N", "M", "C"]
stack5 = ["D", "Z", "B"]
stack6 = ["V", "C", "W", "Z"]
stack7 = ["G", "Z", "N", "C", "V", "Q", "L", "S"]
stack8 = ["L", "G", "J", "M", "D", "N", "V"]
stack9 = ["T", "P", "M", "F", "Z", "C", "G"]

stacks = {1: stack1, 2: stack2, 3: stack3, 4: stack4, 5: stack5, 6: stack6, 7: stack7, 8: stack8, 9: stack9}

input = open('input.txt', 'r')
data = input.readlines()

for line in data:
    #parse line data
    currLine = line.partition("move ")[2]
    quantity = int(currLine.partition(" ")[0])
    currLine = currLine.partition(" from ")[2]
    origin = int(currLine.partition(" ")[0])
    destination = int(currLine.partition(" to ")[2])
    
    for x in range(0, quantity):
        stacks[destination].append(stacks[origin].pop())

answer = ""
for x in stacks:
    answer+=(str(stacks[x].pop()))

print(answer)


#part 2
"""
stack1 = ["B", "P", "N", "Q", "H", "D", "R", "T"]
stack2 = ["W", "G", "B", "J", "T", "V"]
stack3 = ["N", "R", "H", "D", "S", "V", "M", "Q"]
stack4 = ["P", "Z", "N", "M", "C"]
stack5 = ["D", "Z", "B"]
stack6 = ["V", "C", "W", "Z"]
stack7 = ["G", "Z", "N", "C", "V", "Q", "L", "S"]
stack8 = ["L", "G", "J", "M", "D", "N", "V"]
stack9 = ["T", "P", "M", "F", "Z", "C", "G"]

stacks = {1: stack1, 2: stack2, 3: stack3, 4: stack4, 5: stack5, 6: stack6, 7: stack7, 8: stack8, 9: stack9}

input = open('input.txt', 'r')
data = input.readlines()

for line in data:
    #parse line data
    currLine = line.partition("move ")[2]
    quantity = int(currLine.partition(" ")[0])
    currLine = currLine.partition(" from ")[2]
    origin = int(currLine.partition(" ")[0])
    destination = int(currLine.partition(" to ")[2])
    
    loadedCrates = []
    for x in range(0, quantity):
        loadedCrates.append(stacks[origin].pop())
    for x in range(0, quantity): 
        stacks[destination].append(loadedCrates.pop())


answer = ""
for x in stacks:
    answer+=(str(stacks[x].pop()))

print(answer)
"""