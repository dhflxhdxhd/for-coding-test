num = int(input())
line = 1

while num > line:
    num -= line
    line += 1

if line%2 == 0:
    a = num
    b = line+1-num
else:
    a = line+1-num
    b = num

print(f'{a}/{b}')