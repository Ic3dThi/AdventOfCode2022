#Advent of Code 2022 12 02
#Author: ya boi
inputFile = open("adventOfCode_Day02_Input.txt", "r")
inputList = inputFile.readlines()
rpsScores = {"X": 1,"Y": 2, "Z": 3}
rpsDict1 = {"X" : {"A": 3, "B": 0, "C": 6}, "Y": {"A": 6, "B": 3, "C": 0}, "Z": {"A": 0, "B": 6, "C": 3}}
rpsDict2 = {"X" : {"A": 3 + 0, "B": 1 + 0, "C": 2 + 0}, "Y": {"A": 1 + 3, "B": 2 + 3, "C": 3 + 3}, "Z": {"A": 2 + 6, "B": 3 + 6, "C": 1 + 6}}
score1 = 0
score2 = 0
for line in inputList:
    score1 += rpsScores[line[2]] + rpsDict1[line[2]][line[0]]
    score2 += rpsDict2[line[2]][line[0]]
print("Part 1: " + str(score1))
print("Part 2: " + str(score2))
inputFile.close()