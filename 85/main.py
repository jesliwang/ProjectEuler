# n * m *(n+1)*(m+1) / 4 == number
n = 3000
gap = 90000000
target = 8000000
mul = 3000
result = 0
rx = 0
ry = 0
for x in range(1, 3000):
	for y in range(1, 3000):
		supplier = x * y * (x +1) * (y+1)
		diff = abs(supplier - target)
		if( diff < gap ):
			gap = diff
			result = x * y
			rx=x
			ry=y

print(result,",",gap,",",rx,":",ry)
			
