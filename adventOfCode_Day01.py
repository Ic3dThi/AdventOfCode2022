#Advent of Code 2022 Dec 01
#Author: ya boi
inputFile = open("adventOfCodeInput_Day01.txt", 'r')
inputList = inputFile.readlines()
max = 0
curr = 0
for line in inputList:
    if line == "\n":
        curr = 0
    else:
        curr += int(line)
    if curr > max:
        max = curr
print(max)