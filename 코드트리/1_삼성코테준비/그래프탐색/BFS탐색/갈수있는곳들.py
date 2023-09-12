from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

q = deque()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n 

def bfs():
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if in_range(nx, ny) and not grid[nx][ny] and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1




# k개 시작점에서 동시에 진행
for _ in range(k):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    
    visited[r][c] = 1
    q.append((r, c))

bfs()

ans = sum([1 for i in range(n) for j in range(n) if visited[i][j]])

print(ans)