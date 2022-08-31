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

