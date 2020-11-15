import time
start_time = time.time()
s = input()
string = []
num = 0

for i in s:
  # isalpha()함수
    if i.isalpha():
        string.append(i)
    else:
        num += int(i)

string.sort()


print(''.join(string),end="")
print(num)

end_time = time.time()
print("time:",end_time-start_time)



