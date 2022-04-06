# 프린터

def solution(priorities, location):
    answer = []
    num_index = [i for i in range(len(priorities))]
    idx = 0
    
    while priorities:
        check = True
        num = priorities.pop(0)
        for p in priorities:
            if num < p:
                priorities.append(num)
                idx = num_index.pop(0)
                num_index.append(idx)
                check = False
                break
        if check:
            idx = num_index.pop(0)
            answer.append(idx)

        for ans in answer:
            if ans == location:
                return answer.index(ans) + 1
    
print(solution([1,1,9,1,1,1],0))