# 백트레킹 + BFS


# m개의 돌만 적절히 치워 k개의 시작점으로부터 상하좌우 인접한 곳 이동
from collections import deque

n, k, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
# 동시에 출발
starts = [list(map(int, input().split())) for _ in range(k)]
remove = [[0]*n for _ in range(n)]
visited = [[0]*n for _ in range(n)]
ans = 0
# 1. 빼낼 돌을 m개만큼 찾는다 => 백트레킹
# 2. 연결되는 최대값을 찾는다
def clear_starts():
    global q
    q.clear()
    for x, y in starts:
        q.append((x-1, y-1))
        visited[x-1][y-1] = 1

q = deque()
clear_starts()
# print(q)
dxs = [-1, 1, 0, 0]
dys = [0, 0, 1, -1]




def clear_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def bfs():
    while len(q):
        x, y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            
            if in_range(nx, ny) and grid[nx][ny] == 0 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
                
def check_max():
    global max_cnt
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 1:
                cnt += 1
    
    max_cnt = max(max_cnt, cnt)


max_cnt = 0
def backtracking(cnt):
    global q
    if cnt == m:
        clear_visited()
        clear_starts()
        bfs()
        check_max()
        return

    for i in range(n):
        for j in range(n):
            # 출발점에 포함되지 않고, 돌이 있되, 제거되어있지 않은 경우
            # print(q)
            if (i, j) not in q and grid[i][j] == 1 and remove[i][j] == 0 :
                remove[i][j] = 1
                grid[i][j] = 0
                backtracking(cnt+1)
                remove[i][j] = 0
                grid[i][j] = 1



backtracking(0)
print(max_cnt)