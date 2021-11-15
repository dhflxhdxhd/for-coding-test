import math
m,n = map(int,input().split())

def isPrime(num):
    if num == 1:
        return False
    else: 
        for j in range(2,int(math.sqrt(num))+1):
            if num % j == 0:
                return False
        return True
               
                
for i in range(m,n+1):
    if isPrime(i):
        print(i)