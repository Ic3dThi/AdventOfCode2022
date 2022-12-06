#Advent of Code 2022 12 06
#Author: ya boi
inputFile = open("adventOfCode_Day06_Input.txt", "r")
inputList = inputFile.readlines()
class Day06():
    def __init__(self):
        pass
    def p1(self):
        line = inputList[0]
        test = ""
        maxLength = -1
        for x in range(len(line)):
            c = list(line)[x]
            current = "".join(c)
            if (current in test):
                test = test[test.index(current) + 1:]
            test = test + "".join(c)
            maxLength = max(len(test), maxLength)
            if maxLength == 4:
                print(x+1)
                break
    def p2(self):
        line = inputList[0]
        test = ""
        maxLength = -1
        for x in range(len(line)):
            c = list(line)[x]
            current = "".join(c)
            if (current in test):
                test = test[test.index(current) + 1:]
            test = test + "".join(c)
            maxLength = max(len(test), maxLength)
            if maxLength == 14:
                print(x+1)
                break
output = Day06()
output.p1()
output.p2()