from collections import deque

n = int(input())
grid = [['']*n for _ in range(n)]

for i in range(n):
    string = input()
    for j in range(n):
        grid[i][j] = string[j]

# print(grid)
walls = []
for i in range(n):
    # print(grid[i])
    for j in range(n):
        # print(grid[i][j])
        if grid[i][j] == ".":
            grid[i][j] = 0
        else:
            grid[i][j] = 1
            walls.append((i, j))

visited = [[0]*n for _ in range(n)]
choose_wall = []

q = deque()

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs():
    while q:
        x, y = q.popleft()
        # print(x, y)
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if (nx, ny) in choose_wall:
                q.append((nx, ny))
                visited[nx][ny] = 1

            if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = 1


    # print(grid, visited)
    # 모든 벽이 이어졌는지 확인
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0 and not visited[i][j]:
                return False

    return True



# 최소 몇개의 벽을허물어야 하나
# 최소 벽의 수가 6개 넘으면 -1 출력
result = 987654321
is_link = True
# 1. 무너뜨릴 벽을 선택한다 (1개 ~ 6개까지)
def choose(cnt, num):
    global result

    if cnt == 7:
        result = -1
        return

    if cnt == num:
        # print(choose_wall)
        for i in range(n):
            for j in range(n):
                visited[i][j] = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visited[i][j] = 1
                    is_link = bfs()
                    break
            break

        if is_link:
            # print(visited)

            result = min(result, num)

        return

    for i in range(len(walls)):
        if visit_wall[i]:
            continue

        grid[walls[i][0]][walls[i][1]] = 0
        visit_wall[i] = 1
        choose(cnt+1, num)
        grid[walls[i][0]][walls[i][1]] = 1
        visit_wall[i] = 0

visit_wall = [0] * len(walls)

for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            q.append((i, j))
            visited[i][j] = 1
            break
        break

if bfs():
    result = 0
else:
    for num in range(1, 8):
        choose(0, num)

print(result)