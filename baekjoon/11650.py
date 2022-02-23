n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

arr = sorted(arr, key=lambda arr: (arr[0],arr[1]))
print(arr)