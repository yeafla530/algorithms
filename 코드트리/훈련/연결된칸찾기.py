from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
q = deque([])

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs():
    global count
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if in_range(nx, ny) and grid[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append([nx, ny])
                count += 1



def clear_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0

ans = []
for i in range(n):
    for j in range(n):
        
        if grid[i][j] == 1 and visited[i][j] == 0:
            # clear_visited()
            count = 1
            visited[i][j] = 1
            q.append([i, j])
            bfs()

            ans.append(count)

ans.sort()
print(len(ans))
for n in ans:
    print(n)