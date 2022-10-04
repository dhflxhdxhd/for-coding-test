from collections import deque

n, k = map(int, input().split())
list = [i+1 for i in range(n)]

queue = deque(list)
ans = []

while queue:
    for i in range(k-1):
        queue.append(queue.popleft())

    ans.append(queue.popleft())


print("<", end = "")
for i in range(n):
    print(ans[i], end=", ")
print(">")










