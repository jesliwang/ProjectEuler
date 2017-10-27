import os, sys

result = pow(2, 1000)
sum = 0

while result > 0:
    sum += result % 10
    result /= 10

print sum
