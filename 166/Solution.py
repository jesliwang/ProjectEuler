'''
a b c d = x
e f g h = x
i j k l = x
m n o p = x
a f k p = x
d g j m = x
a e i m = x
b f j n = x
c g k o = x
d h l p = x

a b c d e f g i 

m j n h p

b c d = f k p
b c d = e i m
c k o = e f h 

'''

def GetNext(lst):
    index = 0
    while index < len(lst):
        if lst[index] < 9:
            lst[index] += 1
            break
        else:
            lst[index] = 0
        index += 1
    if index >= len(lst):
        return False
    else:
        return True


keys = [ 0 for i in range(8)]
keys[0] = -1
count = 0

while GetNext(keys):
    a = keys[0]
    b = keys[1]
    c = keys[2]
    d = keys[3]
    e = keys[4]
    f = keys[5]
    g = keys[6]
    i = keys[7]
    m = b + c + d - e - i
    if not ( m >= 0 and m <= 9):
        continue
    
    j = a + b + c - m - g
    if not ( j >= 0 and j <= 9):
        continue

    n = a + c + d - f - j
    if not ( n >= 0 and n <= 9):
        continue

    h = a + b + c + d - e - f - g
    if not ( h >= 0 and h <= 9):
        continue

    l2 = a + a + b + c + f - h - i - j
    if l2 % 2 == 1:
        continue
    l = l2//2
    if not(l >=0 and l <= 9):
        continue

    p = a + b + c - h - l
    if not ( p >= 0 and p <=9):
        continue
    
    k = b + c + d - f - p
    if not (k >=0 and k <=9):
        continue

    o = a + f + k - m - n
    if not (o >=0 and o <=9):
        continue
    
    count += 1

print(count)