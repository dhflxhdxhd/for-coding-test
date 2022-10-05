# 프린터 큐
# https://assaeunji.github.io/python/2020-05-04-bj1966/
from collections import deque

t = int(input())

for i in range(t):
    n,m = map(int, input().split())
    queue = deque(list(input().split()))
    cnt = 0 # 몇 번째로 인쇄되는지 카운트
    
    while queue:
        max_num = max(queue)
        print_num = queue.popleft()
        m = m-1 #index 하나씩 이동
       
        if max_num == print_num :
            cnt += 1
            if m < 0: # 해당 인덱스라는 의미
                print(cnt)
                break
        else:
            queue.append(print_num)
            if m < 0: # 해당 인덱스이면 다시 뒤로 보내야되니까 인덱스 리셋
                m = len(queue) - 1