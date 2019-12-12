
n = 3000
gap = 90000000
target = 8000000
mul = 3000
for x in range(1, 3000):
	for y in range(1, 3000):
		supplier = x * y * (x +1) * (y+1)
		diff = Math.abs(supplier - target)
		if( diff < gap ):
			gap = diff
		else if( diff == gap && mul > x **y)
			
