import numpy

def GetLength(len):
    num_list = numpy.zeros((len,4))

    num_list[0,0] = 1
    for x in range(1, len):
        num_list[x,0] = num_list[x-1,0] + num_list[x-1,1] + num_list[x-1,2] + num_list[x-1,3]
        for gap in range(2,5):
            pre = x - gap
            if pre >= 0:
                sSum = 0
                for sIndex in range(0,4):
                    sSum += num_list[pre,sIndex]
                num_list[x, gap-1] = sSum
            elif pre == -1:
                num_list[x, gap-1] = 1
    return num_list[len-1,0] + num_list[len-1,1] + num_list[len-1,2] + num_list[len-1,3]
print(GetLength(50))

