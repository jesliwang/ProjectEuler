import numpy

def GetColor(len, gap):
    num_list = numpy.zeros((len,2))

    num_list[0,0] = 1
    for x in range(1, len):
        num_list[x,0] = num_list[x-1,0] + num_list[x-1,1]
        pre = x - gap
        if pre >= 0:
            num_list[x, 1] = num_list[pre,0] + num_list[pre,1]
        elif pre == -1:
            num_list[x, 1] = 1

    return num_list[len-1,0] + num_list[len-1,1] - 1

target = 50

print(GetColor(target,2) + GetColor(target,3) + GetColor(target,4)) 
        

