import os, sys
"""
0.12345678910111213
"""

def getNth(n):
    subNth = n
    index = 1

    # find xxxx
    while subNth > index *(pow(10, index ) - pow(10, index - 1)):
        subNth -= (index * (pow(10, index ) - pow(10, index - 1)))
        index += 1

    if index == 1:
        return subNth

    subNth -= 1

    next = subNth / index
    innerIndex = subNth % index

    numberList = []

    targetNumber = pow(10, index - 1) + next

    while targetNumber > 0:
        numberList.append(targetNumber%10)
        targetNumber/=10
    numberList.reverse()

    return numberList[innerIndex]

mul = 1
for index in range(0, 7):
    mul *= getNth(pow(10, index))

print mul
