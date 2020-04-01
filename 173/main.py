import sys

def GetSquareLamina(width, blocks):
    if width <= 2 :
        return 0
    needs = (width - 1) * 4
    if blocks >= needs:
        return 1 + GetSquareLamina(width - 2, blocks - needs)
    else:
        return 0

#blocks = 100
blocks = 1000000
ans = 0
for i in range(3, blocks):
    ans += GetSquareLamina(i, blocks)

print(ans)
    