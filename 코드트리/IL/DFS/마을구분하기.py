n = int(input())
villiage = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def can_go(x, y):
    if not (0 <= x < n and 0 <= y < n):
        return False
    if villiage[x][y] == 0 or visited[x][y]:
        return False
    
    return True
     
# 연결된 사람 찾기
def dfs(x, y):
    global people_num
    for dx,dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if can_go(nx, ny):
            visited[nx][ny] = 1
            people_num += 1
            dfs(nx, ny)
    

people = []
for i in range(n):
    for j in range(n):
        if can_go(i, j):
            visited[i][j] = 1
            people_num = 1
            dfs(i, j)
            people.append(people_num)
    
people.sort()
print(len(people))
for i in people:
    print(i)