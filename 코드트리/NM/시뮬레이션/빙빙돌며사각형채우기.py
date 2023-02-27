n, m = map(int, input().split())
grid = [[0]*m for _ in range(n)]
s = ord('A')
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
dir_num = 0
x, y = 0, 0
grid[x][y] = s

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

count = 1
for i in range(1, n*m):
    nx = x + dxs[dir_num]
    ny = y + dys[dir_num]

    if not (in_range(nx, ny)) or grid[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4       

    x = x + dxs[dir_num]
    y = y + dys[dir_num]
    
    s += 1

    if s > ord('Z'):
        s = ord('A')
    grid[x][y] = s

for i in range(n):
    for j in range(m):
        print(chr(grid[i][j]), end=" ")
    print()

