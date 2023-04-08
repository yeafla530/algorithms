# 오른쪽, 아래, 왼쪽, 위 순서
# 1. 격자 벗어나는지, 이미 방문한 곳 아닌지

n, m = map(int, input().split())
answer = [[0]*m for _ in range(n)]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0
dir_num = 0

answer[x][y] = 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for i in range(2, n*m+1):
    nx = x + dxs[dir_num]
    ny = y + dys[dir_num]

    if not in_range(nx, ny) or answer[nx][ny] != 0:
        dir_num = (dir_num+1) % 4
    
    x = x + dxs[dir_num]
    y = y + dys[dir_num]

    answer[x][y] = i


print(answer)

for i in range(n):
    for j in range(m):
        print(answer[i][j], end=" ")
    print()


n = int(input())
answer = [[0]*n for _ in range(n)]
# 왼 위 오 아
dxs = [0, -1, 0, 1]
dys = [-1, 0, 1, 0]

x, y = n-1, n-1
dir_num = 0
answer[x][y] = n*n

for i in range(n*n-1, 0, -1):
    nx = x + dxs[dir_num]
    ny = y + dys[dir_num]

    if not in_range(nx, ny) or answer[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
    x = x + dxs[dir_num]
    y = y + dys[dir_num]

    answer[x][y] = i
   
for i in range(n):
    for j in range(n):
        print(answer[i][j], end=" ")
    print()