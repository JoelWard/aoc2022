input = open('input.txt', 'r')
data = input.readlines()

directorySizes = []
workingDirectory = []

dataSize = 0
index = 0;

for line in data:
    if (line == "$ cd ..\n"):
        workingDirectory.pop()
    elif (line[0:4] == "$ cd"):
        workingDirectory.append(line[5:len(line)-1] + str(index))
        directorySizes.append([line[5:len(line)-1] + str(index),0])
    elif (line[0:3] != "dir" and line[0:4] != "$ ls"):
        for directory in workingDirectory:
            for x in range(0,len(directorySizes)):
                if (directory == directorySizes[x][0]):
                    directorySizes[x][1]+=int(line.partition(" ")[0])
    index+=1

for directory in directorySizes:
    if directory[1] <= 100000:
        dataSize+=directory[1]

print(dataSize)

storageUsed = 0

for x in range(0,len(directorySizes)):
    if ("/0" == directorySizes[x][0]):
        storageUsed = directorySizes[x][1]

freeStorage = 70000000 - storageUsed

storageNeeded = 30000000 - freeStorage

currFileSize = 70000000

for x in range(0,len(directorySizes)):
    if (directorySizes[x][1] < currFileSize and directorySizes[x][1] > storageNeeded):
       currFileSize = directorySizes[x][1]

print(currFileSize)