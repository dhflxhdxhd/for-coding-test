#heapq 라이브러리
#heapq.heappush()
#heapq.heappop()

#힙정렬
import heapq

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h,value)
    
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

arr = [1,3,5,7,9,2,4,6,8,0]
result = heapsort(arr)
print(result)