from collections import deque

n = int(input())
grid = [list(map(int, input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

blocks = []

dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs():
    count = 0
    while q:
        x, y = q.popleft()
        count += 1
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1

    blocks.append(count)

cnt = 0
for i in range(n):
    for j in range(n):
        # print(grid[i][j])
        if grid[i][j] == 1 and not visited[i][j]:
            cnt += 1
            q = deque()
            q.append((i, j))
            visited[i][j] = 1
            bfs()

blocks.sort()
print(cnt)
for i in range(cnt):
    print(blocks[i])