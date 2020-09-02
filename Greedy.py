# 그리디 greedy 알고리즘
# 가장 큰 순서대로
n = 1260
count = 0

list = [500,100,50,10]

for coin in list:
    count += n
    n %= coin

print(count)