n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
result = 0
# 밖으로 떨어진 먼지 양
arr = [(0, 0, 0) for _ in range(n*n)]
visited = [[0]*n for _ in range(n)]
next_grid = [[0]*n for _ in range(n)]
# 우 하 좌 상
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

x = 0
y = 0
dir_num = 0
visited[0][0] = 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for i in range(n*n-2, -1, -1):
    nx = x + dxs[dir_num]
    ny = y + dys[dir_num]

    if not in_range(nx, ny) or visited[nx][ny]:
        dir_num = (dir_num + 1) % 4
        nx = x + dxs[dir_num]
        ny = y + dys[dir_num]

    arr[i] = (nx, ny, dir_num^2)
    visited[nx][ny] = 1
    x = nx
    y = ny

# print(arr)

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for i in range(len(arr)-1):
    # 먼지 계산하기
    x, y, d = arr[i]
    nx, ny, nd = arr[i+1]
    dirty = grid[nx][ny]
    add_dirty = 0

    grid[nx][ny] = 0

    # for i in range(n):
    #     for j in range(n):
    #         next_grid[i][j] = 0

    # 범위를 벗어났을 때 result에 더해줌
    # 1 3 5 3 으로 줄어듦
    for a in range(1, 2):
        right = (d + 1) % 4
        left = (d - 1) % 4

        ax = x + (dxs[right] * a)
        ay = y + (dys[right] * a)

        bx = x + (dxs[left] * a)
        by = y + (dys[left] * a)

        if in_range(ax, ay):
            # next_grid[ax][ay] += int(dirty * 0.01)
            grid[ax][ay] += int(dirty * 0.01)

        else:
            result += int(dirty * 0.01)

        add_dirty += int(dirty * 0.01)

        if in_range(bx, by):
            # next_grid[bx][by] += int(dirty * 0.01)
            grid[bx][by] += int(dirty * 0.01)

        else:
            result += int(dirty * 0.01)

        add_dirty += int(dirty * 0.01)


    for a in range(1, 3):
        right = (d + 1) % 4
        left = (d - 1) % 4

        ax = nx + (dxs[right] * a)
        ay = ny + (dys[right] * a)

        bx = nx + (dxs[left] * a)
        by = ny + (dys[left] * a)
        percent = 0
        if a == 1:
            percent = 0.07
        else:
            percent = 0.02

        if in_range(ax, ay):
            # next_grid[ax][ay] += int(dirty * percent)
            grid[ax][ay] += int(dirty * percent)

        else:
            result += int(dirty * percent)

        add_dirty += int(dirty * percent)

        if in_range(bx, by):
            # next_grid[bx][by] += int(dirty * percent)
            grid[bx][by] += int(dirty * percent)

        else:
            result += int(dirty * percent)

        add_dirty += int(dirty * percent)

    for a in range(1, 2):
        right = (d + 1) % 4
        left = (d - 1) % 4

        ax = nx + dxs[d] + (dxs[right] * a)
        ay = ny + dys[d] + (dys[right] * a)

        bx = nx + dxs[d] + (dxs[left] * a)
        by = ny + dys[d] + (dys[left] * a)
        percent = 0.1

        if in_range(ax, ay):
            # next_grid[ax][ay] += int(dirty * percent)
            grid[ax][ay] += int(dirty * percent)

        else:
            result += int(dirty * percent)

        add_dirty += int(dirty * percent)

        if in_range(bx, by):
            # next_grid[bx][by] += int(dirty * percent)
            grid[bx][by] += int(dirty * percent)

        else:
            result += int(dirty * percent)

        add_dirty += int(dirty * percent)


    for a in range(1):
        ax = nx + (dxs[d] * 2)
        ay = ny + (dys[d] * 2)

        percent = 0.05

        if in_range(ax, ay):
            # next_grid[ax][ay] += int(dirty * percent)
            grid[ax][ay] += int(dirty * percent)
        else:
            result += int(dirty * percent)

        add_dirty += int(dirty * percent)

    if in_range(nx+dxs[d], ny+dys[d]):
        # next_grid[nx + dxs[d]][ny + dys[d]] += dirty - add_dirty
        grid[nx + dxs[d]][ny + dys[d]] += dirty - add_dirty

    else:
        result += dirty - add_dirty



    # print(grid)
    # 더해주기
    # for i in range(n):
    #     for j in range(n):
    #         grid[i][j] += next_grid[i][j]


print(result)