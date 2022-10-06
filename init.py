# 프린터 큐
t = int(input())

for i in range(t):
    n,m = map(int, input().split())
    queue = list(input().split())
    idx = [i for i in range(n)]
    idx[m] = "target"
    cnt = 0 # 몇 번째로 인쇄되는지 카운트
    
    while queue:
        max_num = max(queue)
        if max_num == queue[0]:
            cnt += 1
            if idx[0] == "target":
                print(cnt)
                break

            queue.pop(0)
            idx.pop(0)
            
        else:
            queue.append(queue.pop(0))
            idx.append(idx.pop(0))
            