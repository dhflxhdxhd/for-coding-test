#완전탐색
#소수 찾기
from itertools import permutations
import math

def isPrime(num):
    if(num == 1 or num == 0): return False
    else:
        for k in range(2,int(math.sqrt(num))+1):
            if num % k == 0:
                return False
        return True

def solution(numbers):
    num = [num for num in numbers]
    per_list = []
    ans = []
    
    for i in range(len(num)):
        per_list += list(permutations(num, i+1))
    num_list = [int("".join(per))for per in per_list]
    # print(num_list)

    for num in num_list:
        if isPrime(num):
            ans.append(num)

    return len(set(ans))
    
print(solution("011"))