# 코딩테스트 연습
# 월간 코드 챌린지 시즌1
# 두 개 뽑아서 더하기

#테스트케이스 3,4 error
def solution(numbers):
    ans = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j :
                ans.append(numbers[i]+numbers[j])

    answer = set(ans)
    return list(answer)

print(solution([5,0,2,7]))