#Advent of Code 2022 12 07
#Author: ya boi
inputFile = open("adventOfCode_Day07_Input.txt", "r")
inputList = inputFile.readlines()
eachDirSize = []

class node():
    def __init__(self, inputName = ""):
        self.name = inputName
        self.size = 0
        self.children = dict()
        self.prev = None
def p1():
    total = 0
    root = None
    sum = 0
    for line in inputList:
        line = line.strip()
        curr = line.split(' ')
        if curr[0] == '$' and curr[1] == 'cd':
            if root == None:
                root = node(curr[2])
            elif curr[2] == '..':
                temp = root.size
                eachDirSize.append(temp)
                if int(temp) <= 100000:
                    sum += int(temp)
                root = root.prev
                root.size += temp
            else:
                root = root.children[curr[2]]
        elif curr[0] == 'dir':
            child = node(curr[1])
            child.prev = root
            root.children[child.name] = child
        elif curr[0].isdigit():
            root.size += int(curr[0])
            total += int(curr[0])
    print(sum)
    return total

def p2(total):
    eachDirSize.sort()
    sizeNeeded = 30000000 - (70000000 - total)
    for x in eachDirSize:
        if x > sizeNeeded:
            print(x)
            break

total = p1()
p2(total)