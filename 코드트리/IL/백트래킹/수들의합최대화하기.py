n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n

max_num = 0
# 각 행과 열에 1개씩 
def choose(cnt, val):
    global max_num
    if cnt == n:
        max_num = max(max_num, val)
        return
    
    for j in range(n):
        if visited[j]:
            continue
        visited[j] = True
        choose(cnt+1, val+arr[cnt][j])
        visited[j] = False
        


choose(0, 0)
print(max_num)