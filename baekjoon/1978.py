#소수찾기

n = int(input())
nums = map(int, input().split())

for num in nums:
    if num == 1:
        return False
    elif num == 2:
        return True
    
    for i in range(2, num)
        if num % i ==0 :
            return False
    return True