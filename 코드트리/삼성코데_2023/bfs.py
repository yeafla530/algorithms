from collections import deque


dxs = [-1, 1, 0, 0]
dys = [0, 0, 1, -1]

def bfs():
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if in_range(nx, ny) and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1


for _ in range(k):
    x, y = map(int, input().split())
    x -= 1
    y -= 1

    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    bfs()