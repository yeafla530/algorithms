import sys
from collections import deque

INT_MAX = sys.maxsize

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))

a = [
    list(map(int, input().split()))
    for _ in range(n)
]

# bfs에 필요한 변수들 입니다.
q = deque()
visited = [[0]*m for _ in range(n)]
# 최단거리 구하기
step = [[-1]*m for _ in range(n)]

ans = INT_MAX


def can_go(x, y):
    return 0 <= x < n and 0 <= y < m and not visited[x][y] and a[x][y]

def push(x, y, s):
    step[x][y] = s
    visited[x][y] = 1
    q.append((x, y))



dxs = [0, -1, 0, 1]
dys = [1, 0, -1, 0]

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            
            if can_go(nx,ny):
                push(nx, ny, step[x][y]+1)



visited[0][0] = 1
step[0][0] = 0
q.append((0, 0))
bfs()
print(step[n-1][m-1])