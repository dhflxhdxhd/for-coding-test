# 부녀회장이 될테야

T=int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    rnum = [i for i in range(1,n+1)]
    for _ in range(k):
        for j in range(1,n):
            rnum[j] += rnum[j-1]
    print(rnum[-1])        