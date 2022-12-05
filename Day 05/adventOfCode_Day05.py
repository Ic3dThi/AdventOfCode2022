#Advent of Code 2022 12 05
#Author: ya boi
inputFile = open("adventOfCode_Day05_Input.txt", "r")
inputList = inputFile.readlines()
class Day05():
    def __init__(self):
        pass
    def noCrate(self, stack, crate):
        if crate != ' ':
            stack.append(crate)

    def p1(self):
        outputStr = ""
        stacks = [[], [], [], [], [], [], [], [], []]
        for line in inputList:
            if line[0] == '[':
                for i in range(9):
                    self.noCrate(stacks[i], line[i * 4 + 1])
            if line[0] == 'm':
                currLine = line.split(' ')
                for j in range(int(currLine[1])):
                    stacks[int(currLine[5][0]) - 1].insert(0, stacks[int(currLine[3]) - 1][0])
                    stacks[int(currLine[3]) - 1] = stacks[int(currLine[3]) - 1][1:]
        for stack in stacks:
            outputStr += stack[0]
        print(outputStr)
    def p2(self):
        outputStr = ""
        stacks = [[],[],[],[],[],[],[],[],[]]
        for line in inputList:
            if line[0] == '[':
                for i in range(9):
                    self.noCrate(stacks[i], line[i*4+1])
            if line[0] == 'm':
               currLine = line.split(' ')
               stacks[int(currLine[5][0]) - 1][:0] = stacks[int(currLine[3])-1][:int(currLine[1])]
               stacks[int(currLine[3]) - 1] = stacks[int(currLine[3])-1][int(currLine[1]):]
        for stack in stacks:
            outputStr += stack[0]
        print(outputStr)
output = Day05()
output.p1()
output.p2()