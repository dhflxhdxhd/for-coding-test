n,m = list(map(int,input().split()))
s = []
def BT():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            BT()
            s.pop()
BT()
 
