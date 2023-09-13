# 백준 단지번호 붙이기
from collections import deque

n = int(input())
grid = [list(map(int, input())) for _ in range(n)]
answer = []
q = deque()
visited = [[0]*n for _ in range(n)]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(cnt):
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 1:
                cnt += 1
                q.append((nx, ny))
                visited[nx][ny] = 1

    answer.append(cnt)

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            visited[i][j] = 1
            q.append((i, j))
            bfs(1)


answer.sort()

print(len(answer))
for x in answer:
    print(x)


