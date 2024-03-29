# 11060. 점프점프
# dp

n = int(input())
maze = list(map(int,input().split(" ")))
dp = [n+1]*n
dp[0] = 0

for i in range(n):
    for j in range(1,maze[i]+1):
        if i+j >= n:
            break
        dp[i+j] = min(dp[i+j], dp[i]+1)

if dp[-1] == n+1:
    print(-1)
else:
    print(dp[-1])


