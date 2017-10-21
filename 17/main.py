import os, sys

characDic = {
 1 : "one",
 2 : "two",
 3 : "three",
 4 : "four",
 5 : "five",
 6 : "six",
 7 : "seven",
 8 : "eight",
 9 : "nine",
 10 : "ten",
 11 : "eleven",
 12 : "twelve",
 13 : "thirteen",
 14 : "fourteen",
 15 : "fifteen",
 16 : "sixteen",
 17 : "seventeen",
 18 : "eighteen",
 19 : "nineteen",
 20 : "twenty",
 30 : "thirty",
 40 : "forty",
 50 : "fifty",
 60 : "sixty",
 70 : "seventy",
 80 : "eighty",
 90 : "ninety"
}

def num_letter_coun(num):
    if characDic.has_key(num):
        return len(characDic[num])
    else:
        if num < 100:
            return len(characDic[num%10]) + len(characDic[num-num%10])
        elif num < 1000:
            if num % 100 != 0:
                return len(characDic[num/100]) + len("hundred") + len("and") + num_letter_coun(num%100)
            else:
                return len(characDic[num/100]) + len("hundred")
        else:
            return 0


result = num_letter_coun(1) + len("thousand")
print result
for index in range(1, 1000):
    result += num_letter_coun(index)

print num_letter_coun(342)
print num_letter_coun(115)
print result
