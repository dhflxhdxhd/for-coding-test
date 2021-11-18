#골드바흐의 추측
#유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다.

#나의 생각 

# t = int(input())
import math
def isPrime(st):
    for j in range(2,int(math.sqrt(st))+1):
        if st%j == 0:
            return False
    return True

st = 2
n = int(input())
while True:
    if isPrime(st):
        n -= st
        print(n)
        print(st)
        if isPrime(n):
            break
        else:
            st += 1

print("n"+str(n)+" st"+str(st))

