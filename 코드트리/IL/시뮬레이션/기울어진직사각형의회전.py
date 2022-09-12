n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, move_dir = map(int, input().split())
change = [[0]*n for _ in range(n)]

r = r-1
c = c-1

def shift_box(r, c, m1, m2, move_dir):
    
    temp = grid[r][c]
    # 시계방향
    if move_dir:
        dxs = [-1, -1, 1, 1]
        dys = [-1, 1, 1, -1]
        arr = [m2, m1, m2, m1]

    # 반시계
    else:
        dxs = [-1, -1, 1, 1]
        dys = [1, -1, -1, 1]
        arr = [m1, m2, m1, m2]

    for dx, dy, a in zip(dxs, dys, arr):
        for _ in range(a):
            r = r + dx
            c = c + dy
            change[r][c] = temp
            temp = grid[r][c]
    
    for i in range(n):
        for j in range(n):
            if change[i][j]:
                grid[i][j] = change[i][j]
                


shift_box(r, c, m1, m2, move_dir)

for i in range(n):
    print(*grid[i])