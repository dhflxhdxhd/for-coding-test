#카드 정렬하기
#우선순위 큐 -> heap 이용
import heapq
n =  int(input())

h = []
for _ in range(n):
    heapq.heappush(h,int(input()))

result = 0
while len(h) != 1:
    one = heapq.heappop(h)
    two = heapq.heappop(h)
    sum_value = one + two
    result += sum_value
    heapq.heappush(h,sum_value)

print(result)