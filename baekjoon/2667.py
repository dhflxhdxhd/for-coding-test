n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

cnt = []

def dfs(graph,x,y,i):
    global cnt
    if x<=-1 or x>=n or y<=-1 or y>=n:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 2
        cnt[i]
        dfs(graph,x-1, y,i)
        dfs(graph,x+1, y,i)
        dfs(graph,x,y-1,i)
        dfs(graph,x,y+1,i)
        return True
    
    return False

result = 0
num = 0
for i in range(n):
    for j in range(n):
        if dfs(graph,i,j,num) == True:
            result += 1
            num += 1

print(f'result {result}')     
print(f'cnt {cnt}')
