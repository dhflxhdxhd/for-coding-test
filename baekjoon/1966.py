# 프린터 큐
# https://assaeunji.github.io/python/2020-05-04-bj1966/
from collections import deque
n,m = map(int, input().split())
list = list(input().split())

queue = deque(list)
cnt = 0

while queue:
    max_num = max(queue)
    print_num = queue.popleft()
    m = m-1
   
    if max_num == print_num :
        cnt += 1
        if m <  0:
            print(cnt)
            break
    else:
        queue.append(print_num)
        if m < 0:
            m = len(queue) - 1