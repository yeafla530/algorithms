from collections import deque
n, k = map(int, input().split())
geul = [list(map(int, input().split())) for _ in range(n)]
steps = [[-1]*n for _ in range(n)]
visited = [[0]*n for _ in range(n)]
q = deque()


def initial():
    for i in range(n):
        for j in range(n):
            if geul[i][j] == 1:
                steps[i][j] = -2

            elif geul[i][j] == 2:
                q.append((i, j))
                visited[i][j] = 1
                steps[i][j] = 0

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def can_go(x, y):
    return 0 <= x < n and 0 <= y < n and not visited[x][y] and geul[x][y]


def push(x, y, s):
    steps[x][y] = s
    visited[x][y] = 1
    q.append((x, y))

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if can_go(nx, ny):    
                push(nx, ny, steps[x][y] + 1)


initial()
bfs()

for i in range(n):
    print(*steps[i])

