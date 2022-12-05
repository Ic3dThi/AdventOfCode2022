#Advent of Code 2022 12 03
#Author: ya boi
inputFile = open("adventOfCode_Day03_Input.txt", "r")
inputList = inputFile.readlines()
class Day03():
    def __init__(self):
        pass
    def p1(self):
        sum = 0
        for line in inputList:
            com1 = set(line[0:len(line)//2])
            com2 = set(line[len(line)//2:])
            duplicate = com1.intersection(com2)
            if ord(list(duplicate)[0]) > 96:
                sum += ord(list(duplicate)[0]) - 96
            else:
                sum += ord(list(duplicate)[0]) - 38
        print(sum)
    def p2(self):
        sum = 0
        for i in range(0, len(inputList), 3):
            elf1 = set(inputList[i][:-1])
            elf2 = set(inputList[i+1][:-1])
            elf3 = set(inputList[i+2][:-1])
            inter = elf1.intersection(elf2)
            duplicate = inter.intersection(elf3)
            if ord(list(duplicate)[0]) > 96:
                sum += ord(list(duplicate)[0]) - 96
            else:
                sum += ord(list(duplicate)[0]) - 38
        print(sum)
output = Day03()
output.p1()
output.p2()
