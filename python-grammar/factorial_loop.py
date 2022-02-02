#반복적으로 구현
def fac(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    
    return result

print(fac(3))