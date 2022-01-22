#카드 정렬하기
///////////////error
n =  int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()

sum = []
sum.append(arr[0] + arr[1])
for i in range(len(arr)-2):
   sum.append(sum[0] + arr[1] + arr[2])
print(sum)