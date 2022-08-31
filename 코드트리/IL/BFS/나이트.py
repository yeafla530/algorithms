from collections import deque
n = int(input())
r1, c1, r2, c2 = map(int, input().split())
r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

visited = [[0]*n for _ in range(n)]
steps = [[-1]*n for _ in range(n)]
dxs = [-2, -1, 1, 2, 2, 1, -1, -2]
dys = [1, 2, 2, 1, -1, -2, -2, -1]

q = deque()

def can_go(x, y):
    return 0 <= x < n and 0 <= y < n and not visited[x][y]

def push(x, y, s):
    steps[x][y] = s
    visited[x][y] = 1
    q.append((x, y))

def bfs():
    while q:
        x, y = q.popleft()
        # print(x, y)
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if can_go(nx, ny):
                # print(nx, ny)
                push(nx, ny, steps[x][y]+1)


steps[r1][c1] = 0
q.append((r1, c1))
visited[r1][c1] = 1

bfs()
# print(steps)
print(steps[r2][c2])