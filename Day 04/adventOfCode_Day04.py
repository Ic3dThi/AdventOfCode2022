#Advent of Code 2022 12 02
#Author: ya boi
inputFile = open("adventOfCode_Day04_Input.txt", "r")
inputList = inputFile.readlines()
class Day04():
    def __init__(self):
        pass
    def p1(self):
        overlap = 0
        for line in inputList:
            elves = line.split(',')
            elf1 = elves[0].split('-')
            elf2 = elves[1].split('-')
            if (int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1])) or \
                    (int(elf2[0]) >= int(elf1[0]) and int(elf2[1]) <= int(elf1[1])):
                overlap += 1

        print(overlap)

    def p2(self):
        noOverlap = 0
        for line in inputList:
            elves = line.split(',')
            elf1 = elves[0].split('-')
            elf2 = elves[1].split('-')
            if (int(elf1[1]) < int(elf2[0]) and int(elf2[1]) > int(elf1[0])) or (int(elf2[1]) < int(elf1[0]) and int(elf1[1]) > int(elf2[0])):
                noOverlap +=1
        print(len(inputList) - noOverlap)
output = Day04()
output.p1()
output.p2()
