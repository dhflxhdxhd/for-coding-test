n = int(input())
d = [0] * (n+1)

cnt1 = 0
def fib(n):
    global cnt1
    
    if n == 1 or n==2:
        return 1
        
    if d[n] != 0:
        return d[n]

    d[n] = fib(n-1) + fib(n-2)

    return d[n]

dp = [0] * (n+1)
dp[1] = 1
dp[2] = 1
cnt2 = 0
def fibonacci(n):

    global cnt2
    for i in range(3, n+1):
        cnt2 += 1
        dp[i] = dp[i-1] + dp[i-2]

    return cnt2
    
print(fib(n),fibonacci(n))
print(d)