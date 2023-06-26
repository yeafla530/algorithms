from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1


step = [[0 for _ in range(n)] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

ans = 987654321

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]


blocks = []

# 블록 위치 저장
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            blocks.append((i, j))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

q = deque()

def bfs():
    global ans
    q = deque()
    q.append((r1, c1))

    for (x, y) in arr:
        grid[x][y] = 0

    while q:
        x, y = q.popleft()
        if (x, y) == (r2, c2):
            ans = min(ans, step[x][y])
            break

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
        
            if in_range(nx, ny) and visited[nx][ny] == 0 and grid[nx][ny] == 0:
                q.append((nx, ny))
                step[nx][ny] = step[x][y] + 1
                visited[nx][ny] = 1

    for (x, y) in arr:
        grid[x][y] = 1


    


def initial():
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0
            step[i][j] = 0


arr = []    
def choose(cnt):
    global arr
    if cnt == k:
        initial()
        bfs()
        return
    
    for (x, y) in blocks:
        if (x, y) not in arr:
            arr.append((x, y))
            choose(cnt+1)
            arr.pop()


choose(0)


if ans == 987654321:
    print(-1)

else:
    print(ans)