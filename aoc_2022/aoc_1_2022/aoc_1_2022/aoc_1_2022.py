#Part 1
"""
input = open('input.txt', 'r')
data = input.readlines()
  
calories = 0
high = 0;


for line in data:
    if line == '\n':
        if calories > high:
            high = calories
        calories = 0;

    else:
        calories += int(line)

print(high)
"""


#Part 2
"""
input = open('input.txt', 'r')
data = input.readlines()
  
calories = 0
first = 0;
second = 0;
third = 0;

for line in data:
    if line == '\n':
        if calories > first:
            third = second
            second = first
            first = calories
        elif calories > second:
            third = second
            second = calories
        elif calories > third:
            third = calories
        calories = 0;

    else:
        calories += int(line)

print(first + second + third)
"""