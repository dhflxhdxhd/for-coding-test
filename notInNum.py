# def solution(numbers):
#     answer = 0
#     numbers.sort()
#     arr = [0]*10

#     for n in numbers:
#         arr[n] += 1

#     for i,a in enumerate(arr):
#         if a == 0:
#             answer += i

#     return answer