n,k = map(int,input().split())
queue = [i+1 for i in range(n)]


idx = 0
print("<", end="")
for i in range(n,0,-1):
    idx = (idx + (k-1)) % i

    if len(queue) > 1:
        print(queue.pop(idx), end=", ")
    else:
        print(queue.pop(idx), end="")

print(">")











