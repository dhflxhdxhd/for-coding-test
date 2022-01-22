n = int(input())

arr = []
for i in range(n):
    arr.append(input().split())

array = sorted(arr, key=lambda score : (-int(score[1]), int(score[2]), -int(score[3]), score[0]) )

for a in array:
    print(array[0])