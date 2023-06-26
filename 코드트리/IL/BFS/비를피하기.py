# 사람이 h명 겹치지 않게 서있고, 
# 비를 피할 수 있는 공간의 위치 m개가 주어짐
# 각 사람마다 비를 피할 수 있는 가장 가까운 공간까지 거리 구하기

# 0 = 이동
# 1 = 벽
# 2 = 사람
# 3 = 비를 피할 수 있는 공간

from collections import deque

n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

step = [[0 for _ in range(n)] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
ans = [[0 for _ in range(n)] for _ in range(n)]


dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

q = deque()
def initial():
    for i in range(n):
        for j in range(n):
            step[i][j] = 0
            visited[i][j]= 0


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def bfs():
    num = 0
    while q:
        x, y = q.popleft()
        
        if grid[x][y] == 3:
            num = step[x][y]
            break

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if in_range(nx, ny) and visited[nx][ny] == 0 and grid[nx][ny] != 1:
                q.append((nx, ny))
                step[nx][ny] = step[x][y] + 1
                visited[nx][ny] = 1

    for i in range(n):
        for j in range(n):
            if step[i][j] == 1:
                ans[i][j] = num - 1

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            initial()
            q = deque()
            step[i][j] = 1
            visited[i][j] = 1
            q.append((i, j))
            bfs()

for i in range(n):
    for j in range(n):
        print(ans[i][j], end=" ")
    print()