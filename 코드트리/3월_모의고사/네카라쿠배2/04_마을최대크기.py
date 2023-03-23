from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
q = deque([])

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs():
    global ans
    count = 1
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if in_range(nx, ny) and grid[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                count += 1
                q.append((nx, ny))
    
    ans = max(ans, count)

def clear_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0

ans = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            grid[i][j] = 1
            visited[i][j] = 1
            q.append((i,j))
            bfs()
            clear_visited()
            grid[i][j] = 0
            q = deque([])

print(ans)