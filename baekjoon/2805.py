#2805 나무자르기
n, m = map(int,input().split())
trees = list(map(int,input().split()))

start = 0
end = max(trees)
while start <= end:
    mid = (start + end) // 2
    count = 0
    
    for tree in trees:
        if tree > mid: # 절단기의 높이가 나무보다 작다면
            count += tree - mid

    # count가 충분한 경우 최댓값을 찾기 위해 mid를 하나 증가
    if count >= m:
        result = mid
        start = mid + 1
    # count가 부족한 경우 h를 더 작게.  왼쪽 부분탐색
    else:
        end = mid - 1
        

print(result)
                