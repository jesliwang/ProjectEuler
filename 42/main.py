import os, sys
file = open(os.path.dirname(__file__) + "/words.txt")

def TriNumber(word):
    sum = 0
    for index in range(0, len(word)):
        sum += (ord(word[index]) - ord('A') + 1)

    #print sum
    target = int(pow(2*sum, 0.5))
    if sum * 2 == target * (target + 1):
        return True
    else:
        return False

TriNumber("SKY")

line = file.readline()

num = 0
while line:
    words = line.split(",")

    for index in range(0, len(words)):
        if TriNumber(words[index][1:-1]):
            num += 1

    line = file.readline()

print num
