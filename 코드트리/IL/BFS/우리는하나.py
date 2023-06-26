# 각 칸마다 하나의 도시가 존재
# 도시마다 높이 주어짐
# k개의 도시 겹치지 않게 적절히 골라, k개의 도시로부터 갈 수 있는 서로다른 도시의 수 최대화
# 이동은 상하좌우 인접한 도시간 이동만 가능
# 두 도시 간의 높이 차이가 u이상 d이하인 경우에만도 가능

# 적절히 골라 서로다른 도시의 수 최대로 하는 프로그램
from collections import deque


n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
ans = 0

def initial_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

q = deque()
def bfs():
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if in_range(nx, ny) and not visited[nx][ny] and u <= abs(grid[x][y] - grid[nx][ny]) <= d:
                q.append((nx, ny))
                visited[nx][ny] = 1

    count = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                count += 1

    return count


arr = []
visit = [[0 for _ in range(n)] for _ in range(n)]


def choose(cnt):
    global arr, q, ans
    if cnt == k:
        initial_visited()
        q = deque(arr[:])
        for (x, y) in q:
            visited[x][y] = 1 
        ans = max(ans, bfs())
    
        return

    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                visit[i][j] = 1
                arr.append((i, j))
                choose(cnt+1)
                visit[i][j] = 0
                arr.pop()                
    
choose(0)
print(ans)