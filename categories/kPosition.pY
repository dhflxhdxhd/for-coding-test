# 문제
# 어떤 문자열은 A와 B로만 이루어져 있고 B가 2번만 등장하는 특징이 있다.
# N의 길이를 가진 이 문자열을 사전 순으로 배열할 때, K번째 문자열의 두번째 B의 위치를 구하시오. 

count = 0
n,k = map(int,input().split())

for i in range(1,n):
    num = n+1

    for j in range(i):
        count += 1
        num -= 1

        if count == k:
            print(bin(num))
            break