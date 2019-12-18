
def IsBounce(num):
    if num < 10:
        return False
    else:
        running = num
        preMax = num % 10
        running = num / 10
        result = False
        # 0 none 1 increse -1 decrese
        state = 0
        while running > 0:
            tmp = running % 10
            running = running / 10

            if tmp > preMax:
                if state == 0 or state == 1:
                    state = 1
                    preMax = tmp
                else:
                    result = True
                    break
            elif tmp == preMax:
                continue
            else:
                if state == 0 or state == -1:
                    state = -1
                    preMax = tmp
                else:
                    result = True
                    break
        
        return result

bounce = 0
start = 9
while bounce * 100 != 99 * start:
    start += 1
    if IsBounce(start):
        bounce += 1
    
print(start)

                


