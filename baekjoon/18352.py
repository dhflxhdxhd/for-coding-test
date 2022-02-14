input_data = list(map(int,input().split()))

n = input_data[0]
m = input_data[1]
k = input_data[2]
x = input_data[-1]

graph = [[] for _ in range( n+1) ]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)


