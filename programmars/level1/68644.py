# 코딩테스트 연습
# 월간 코드 챌린지 시즌1
# 두 개 뽑아서 더하기

def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        answer.append(numbers[i]+numbers[i+1])
    return answer

print(solution([2,1,3,4,1]))