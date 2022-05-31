#1931
#회의실 배정
#error
n = int(input())
time_list = []

for i in range(n):
    x,y = map(int,input().split())
    time_list.append([x,y])

time_list.sort(key = lambda x : (x[0], x[1]))

cnt = 0 
end = 0
for s,e in time_list:
    if s  >= end:
        cnt += 1
        end = e
    
print(cnt)