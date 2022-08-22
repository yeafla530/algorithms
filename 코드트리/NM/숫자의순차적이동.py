n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]




def find_center():
    global center
    pos = (0, 0)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == center:
                pos = (i, j)
                center += 1
                return pos

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

dxs = [0, 1, 1, 1, 0, -1, -1, -1]
dys = [1, 1, 0, -1, -1, -1, 0, 1]

def move_all(x, y):
    max_num = 0
    new_pos = (0, 0)
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if in_range(nx, ny) and arr[nx][ny] > max_num:
            max_num = arr[nx][ny]
            new_pos = (nx, ny)
    return new_pos

def change_center(x, y, nx, ny):
    temp = arr[x][y]
    arr[x][y] = arr[nx][ny]
    arr[nx][ny] = temp 


def simulate():
    # center를 찾는다
    x, y = find_center()
    # 8방향 움직인다
    nx, ny = move_all(x, y)
    # 제일 큰값과 바꿔준다
    change_center(x, y, nx, ny)


for _ in range(m):
    center = 1
    for _ in range(n*n):
        simulate()

for i in range(n):
    print(*arr[i][:])        