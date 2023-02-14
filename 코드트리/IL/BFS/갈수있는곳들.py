from collections import deque

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
q = deque()

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    return in_range(x, y) and not graph[x][y] and not visited[x][y]

def bfs():
    global cnt
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = 1


        
for _ in range(k):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    q.append((x, y))
    visited[x][y] = 1
    bfs()

cnt = 0
for i in range(n):
    for j in range(n): 
        cnt += visited[i][j]

print(cnt)


# 풀이 2
from collections import deque


n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
q = deque()

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def can_go(x, y):
    return in_range(x, y) and graph[x][y] == 0 and not visited[x][y]

def bfs():
    global count
    while len(q):
        x, y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = 1
                count += 1




count = 0
for _ in range(k):
    r, c = map(int, input().split())
    r -= 1
    c -= 1

    if can_go(r, c):
        visited[r][c] = 1
        count += 1
        q.append((r, c))
        bfs()

print(count)