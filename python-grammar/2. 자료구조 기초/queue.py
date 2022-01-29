from collections import deque #collections 모듈에서 제공하는 deque 자료구조 사용. 

queue = deque()

queue.append(5)
queue.append(3)
queue.append(2)
queue.append(1)
queue.popleft()
queue.popleft()

print(queue)
queue.reverse()
print(queue)
print(list(queue)) #deque -> list