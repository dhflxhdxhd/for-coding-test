# 1149. RGB 거리
# dp

n = int(input())
dp = [[0,0,0] for i in range(n)]

cost = []
for i in range(n):
    cost.append(list(map(int,input().split())))


dp[0] = cost[0][:]
for i in range(1,n):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + cost[i][2]

print(min(dp[-1]))