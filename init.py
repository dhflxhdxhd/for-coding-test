# 이진탐색
# 방법 1. 재귀함수로 구현

def binary_search(arr,target,start,end):
    mid = (start+end) // 2
    if start > end :
        return None
        
    if array[mid] == target:
        return mid
    if array[mid] > target:
        binary_search(arr,target,start,mid-1)
    else:
        binary_search(arr,target,mid+1,end)

n, target = (list(map(int,input().split())))
array = list(map(int,input().split()))

result = binary_search(array,target,0, n-1)

if result == None:
    print("none")
else:
    print(result + 1)\


;