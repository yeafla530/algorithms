# 시계 반대방향
n, m = map(int, input().split())
arr = [[0]*m for _ in range(n)]

arr[0][0] = 1
# 아 오 위 왼
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

x, y = 0, 0
cur_dir = 0
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

for i in range(2, n*m+1):
    nx = x + dxs[cur_dir]
    ny = y + dys[cur_dir]
    # 영역을 벗어나거나 수가 있으면 회전
    if in_range(nx, ny) and arr[nx][ny] == 0:
        # print('??')
        x, y = nx, ny
        arr[x][y] = i
    else:    
        cur_dir = (cur_dir + 1) % 4
        x = x + dxs[cur_dir]
        y = y + dys[cur_dir]
        arr[x][y] = i
    
    

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()
