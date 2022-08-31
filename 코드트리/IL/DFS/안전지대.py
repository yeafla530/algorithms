import sys
sys.setrecursionlimit(10** 6)

n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

def can_go(x, y, k):
    if not (0 <= x < n and 0 <= y < m):
        return False
    if visited[x][y] or area[x][y] <= k:
        return False
    
    return True

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def dfs(x, y, k):
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if can_go(nx, ny, k):
            visited[nx][ny] = 1
            dfs(nx, ny, k)


max_cnt = 0
num = 1
for k in range(1, 100):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if can_go(i, j, k):
                visited[i][j] = 1
                cnt += 1
                # print(cnt)
                dfs(i, j, k)
    for x in range(n):
        for y in range(m):
            visited[x][y] = 0

    if cnt > max_cnt:
        max_cnt = cnt
        num = k 

# 안전영역수가 최대가 될 때의 K, 그때의 안전영역 수 
print(num, max_cnt)