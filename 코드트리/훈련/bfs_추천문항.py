from collections import deque

n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]
# print(grid)

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

visited = [[0 for _ in range(m)] for _ in range(n)]
ans = 987654321
is_out = False

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs():
    global ans, is_out
    while q:
        x, y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if in_range(nx, ny) and grid[nx][ny] == '.' and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
            
            elif not in_range(nx, ny):
                ans = min(ans, visited[x][y])
                is_out = True
                break

q = deque()
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'J':
            q.append((i, j))
            visited[i][j] = 1
            bfs()


if is_out:
    print(ans)

else:
    print("IMPOSSIBLE")