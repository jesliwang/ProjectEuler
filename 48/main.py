import os, sys

sum = 0
for index in range(1, 1001):
    sum += pow(index, index)

sum %= pow(10, 10)
print sum
