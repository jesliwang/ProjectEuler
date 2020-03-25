import sys

def main(argv = None):
    if argv is None:
        argv = sys.argv

    n = pow(10,7) + 1
    ansMap=[1 for i in range(n)]
    for i in range(2, n):
        if ansMap[i] == 1:
            ansMap[i] = 2
            j = 2
            while i * j < n:
                ct = 0
                nt = i*j
                tt = i*j
                while tt % i == 0:
                    ct += 1
                    tt = tt//i
                ansMap[nt] = ansMap[nt]*(ct+1)
                j = j+1
        
    num = 0
    for i in range(2, n-1):
        if ansMap[i] == ansMap[i+1]:
            num += 1
    print(num)

if __name__ == "__main__":
    sys.exit(main())