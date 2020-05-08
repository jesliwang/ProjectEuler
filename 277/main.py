import sys

def D(num):
    return 3*num

def d(num):
    return (3*num+1)/2    

def U(num):
    return (3*num-2)/4

def R(str, ori):
    o = ori
    flag = True
    for i in range(len(str)-1,-1,-1):
        o = globals()[str[i]](o)
        if o // 1 != o:
            flag = False
    return o, flag

fc = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
#fc = "DdDddUUdDD"
limit = pow(10,15)
#limit = pow(10,6)
for i in range(20000000, 200000000):
    check, flag = R(fc, i)

    if flag and check > limit and check // 1 == check:
        print(check, i)
        break

print("=============")