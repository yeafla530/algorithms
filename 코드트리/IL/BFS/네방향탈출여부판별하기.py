import sys
from collections import deque 
sys.setrecursionlimit(10**6)


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
q = deque()

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    return in_range(x, y) and graph[x][y] and visited[x][y]

def bfs():
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = 1



visited[0][0] = 1
q.append((0, 0))
bfs()

print(visited[n-1][m-1])
