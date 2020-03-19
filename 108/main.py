maxLen = 10000000000

ansGap = 1000

for val in range(ansGap, maxLen+1):
    number = 0
    for x in range(val + 1, 2*val + 1):
        if val * x % (x - val) == 0:
            number += 1
        if number + (2 * val - x) < ansGap:
            break
        if number > ansGap:
            break
    
    if number > ansGap:
        print(val)
        break


# for 1000  ans 180180 --- cost 125m4.478s


        
        

