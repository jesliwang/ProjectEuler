import sys,os

file = open(os.path.dirname(__file__) + "/p102_triangles.txt")

line = file.readline()

def dot(xA, yA, xB, yB):
    return xA * yB - yA * xB

sumNumber = 0
while line:
    data = line.split(',')
    dot1 = dot(int(data[2]) - int(data[0]), int(data[3]) - int(data[1]), -int(data[0]), -int(data[1]))
    dot2 = dot(int(data[4]) - int(data[2]), int(data[5]) - int(data[3]), -int(data[2]), -int(data[3]))
    dot3 = dot(int(data[0]) - int(data[4]), int(data[1]) - int(data[5]), -int(data[4]), -int(data[5]))
    if dot1 * dot2 > 0 and dot2 * dot3 > 0 and dot1 * dot3 > 0:
        sumNumber += 1
    
    line = file.readline()

print sumNumber
