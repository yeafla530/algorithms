
# 나의 풀이1
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

max_cnt = 0
bubble = 0


dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    return in_range(x, y) and graph[x][y] and not visited[x][y]

def dfs(x, y):
    global count
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if can_go(nx, ny) and graph[nx][ny] == graph[x][y]:
            visited[nx][ny] = 1
            count += 1
            dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if can_go(i, j):
            count = 1
            num = graph[i][j]
            visited[i][j] = 1
            
            dfs(i ,j)

            max_cnt = max(max_cnt, count)
            if count >= 4:
                bubble += 1

print(bubble, max_cnt)


# 나의풀이2
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

# dfs는 재귀 사용
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def can_go(x, y, num):
    if not (0 <= x < n and 0 <= y < n):
        return False
    
    if visited[x][y] or graph[x][y] != num:
        return False
    
    return True

def dfs(x, y, number):
    global block, boom
    visited[x][y] = 1
   

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if can_go(nx, ny, number):
            visited[nx][ny] = 1
            block += 1
            dfs(nx, ny, number)

    

boom = 0
max_num = 0

for num in range(1, 100):
    for i in range(n):
        for j in range(n):
            block = 1
            if can_go(i, j, num):
                visited[i][j] = 1
                dfs(i, j, num)
            
            if block >= 4:
                boom += 1
            if max_num < block:
                max_num = block

    

print(boom, max_num)

