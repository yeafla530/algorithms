from collections import deque
import sys
INT_MAX = sys.maxsize

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
value = [[INT_MAX]*n for _ in range(n)]
q = deque()
# 공장으로부터 가장 가까운 집까지의 거리가 최대

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def can_go(x, y):
    return 0 <= x < n and 0 <= y < n and graph[x][y] != 1 and not visited[x][y]



def bfs():
    while q:
        x, y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            
            if can_go(nx, ny):
                push(nx, ny, value[x][y] + 1)
        

def push(x, y, new_step):
    q.append((x, y))
    visited[x][y] = True
    value[x][y] = new_step


for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            push(i, j, 0)

bfs()

result = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            result = max(result, value[i][j])
    
print(result)