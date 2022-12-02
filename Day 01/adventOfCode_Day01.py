#Advent of Code 2022 12 01
#Author: ya boi
inputFile = open("adventOfCodeInput_Day01.txt", 'r')
inputList = inputFile.readlines()
curr = 0
elves = []
for line in inputList:
    if line == "\n":
        elves.append(curr)
        curr = 0
    else:
        curr += int(line)
elves.sort(reverse=True)
print("Max: " + str(elves[0]))
print("Top 3 total: " + str(elves[0] + elves[1] + elves[2]))
inputFile.close()