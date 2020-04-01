import sys
sys.path.append("..")
from Common import PrimeUtil

#limit = 30
limit = pow(10,8)
_, primeList = PrimeUtil.get_prime_dic_and_list(limit)

print("Start Cal:")
head = 0
end = len(primeList) - 1
ans = 0
while head < end:
    while head <= end and primeList[head] * primeList[end] >= limit:
        end -= 1
    if head > end:
        break
    #print(primeList[head], primeList[end])
    ans += (end - head + 1)
    head += 1

print(ans)

