# 33. 퇴사

n = int(input())
ti = []
pi = []
for _ in range(n):
    t,p = map(int,input().split())
    ti.append(t)
    pi.append(p)

dp = pi[:]
for i in range(n,0,-1):
    if (n-i+1)-ti[i-1] >= 0:
        dp[i] = ti[i] + dp[i+ti[i]]
        
