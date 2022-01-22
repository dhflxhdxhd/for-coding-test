n = int(input())

arr = []
for i in range(n):
    input_data = input().split()
    arr.append((input_data[0], int(input_data[1]), int(input_data[2]), int(input_data[3])))

array = sorted(arr, key=lambda score : (-score[1], score[2], -score[3], score[0]) )
print(array)