
def gauss_jordan(m, eps = 1.0/(10**10)):
  """Puts given matrix (2D array) into the Reduced Row Echelon Form.
     Returns True if successful, False if 'm' is singular.
     NOTE: make sure all the matrix items support fractions! Int matrix will NOT work!
     Written by Jarno Elonen in April 2005, released into Public Domain"""
  (h, w) = (len(m), len(m[0]))
  for y in range(0,h):
    maxrow = y
    for y2 in range(y+1, h):    # Find max pivot
      if abs(m[y2][y]) > abs(m[maxrow][y]):
        maxrow = y2
    (m[y], m[maxrow]) = (m[maxrow], m[y])
    if abs(m[y][y]) <= eps:     # Singular?
      return False
    for y2 in range(y+1, h):    # Eliminate column y
      c = m[y2][y] / m[y][y]
      for x in range(y, w):
        m[y2][x] -= m[y][x] * c
  for y in range(h-1, 0-1, -1): # Backsubstitute
    c  = m[y][y]
    for y2 in range(0,y):
      for x in range(w-1, y-1, -1):
        m[y2][x] -=  m[y][x] * m[y2][y] / c
    m[y][y] /= c
    for x in range(h, w):       # Normalize row y
      m[y][x] /= c
  return True

def tenth_poly(k):
    return 1 - k + pow(k, 2) - pow(k, 3) + pow(k, 4) - pow(k, 5) + pow(k, 6) - pow(k, 7) + pow(k, 8) - pow(k, 9) + pow(k, 10)
    #return pow(k,3)

def get_nth_fake(matrix, n, k):
    sum_num = 0
    for index in range(n):
        sum_num += round(matrix[index][n]) * pow(k, index)
    return sum_num

result = 1
for k in range(2, 21):
    matrix = [[pow(j+1,i) for i in range(k+1)] for j in range(k)]
    for i in range(0,k):
        matrix[i][k] = tenth_poly(i+1)

    if gauss_jordan(matrix):
        test_fake = get_nth_fake(matrix, k, k+1)
        ans = tenth_poly(k+1)
        print(test_fake,":",ans)
        if test_fake == ans:
            print(k)
            break
        
        result += test_fake
    else:
        print("Error!!!")
        break

print(result)




