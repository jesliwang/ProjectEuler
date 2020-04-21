'''
3*3 = 9
3b + a*a +b*3 = 8
3d + a*c + b*b + c*a + d*3 = 7
3f + a*e + b*d + c*c + d*b + e*a + f*3 = 6
3h = 5
3j = 4
3l = 3
'''

num = [-1 for i in range(20)]

pos = 0

for i in range(100000, 100000000):
    # 30 or 70
    cur = i*100+70
    squ = cur*cur
    
    tmp = squ // 100
    match = 9
    while tmp % 10 == match:
        tmp //=100
        match -= 1
    if match < 1:
        print(cur,squ)
    if match == 0:
        print(cur,squ)
        break