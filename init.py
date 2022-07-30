import sys
n = int(sys.stdin.readline())
d = [0] * 1000001
def countNum(n):
    if n == 1 or n == 2:
        return n

    if d[n] != 0 :
        return d[n]
    
    d[n] = countNum(n-1) + countNum(n-2)
    return d[n]

print(countNum(n)%15746)