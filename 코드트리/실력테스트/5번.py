from collections import deque 
n = int(input())

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
people = []
q = deque()
for _ in range(3):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    people.append((x, y))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs():
    while q:
        x, y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1

cnt = 0
for i in range(n):
    for j in range(n):
        if (i, j) in people and not visited[i][j]:
            cnt += 1
            visited[i][j]
            q.append((i, j))
            bfs()


if cnt == 3:
    print(1)
else:
    print(0)