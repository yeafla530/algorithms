n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 우 하 좌 상
# dice = {1: [4, 5, 3, 2], 2: [4, 1, 3, 6], 3: [2, 1, 5, 6], 4: [6, 5, 1, 2], 5: [3, 1, 4, 6], 6: [3, 5, 4, 2]}
top = 1
front = 2
right = 3
bottom = 7 - top

dir_idx = 0
q = []
# 시계방향 => 우 하 좌 상
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
visited = [[0] * n for _ in range(n)]

cur_x, cur_y = 0, 0
cur_num = 0
ans = 0


# 1. 주사위 움직이기
def move_dice():
    global top, right, front, bottom, cur_x, cur_y, dir_idx
    # 현재 좌판 위치 구하기
    nx = cur_x + dxs[dir_idx]
    ny = cur_y + dys[dir_idx]

    # 격자판 벗어나는 경우 => 180도 회전
    if not in_range(nx, ny):
        dir_idx += 2
        dir_idx = dir_idx % 4

    cur_x = cur_x + dxs[dir_idx]
    cur_y = cur_y + dys[dir_idx]

    # print(cur_x, cur_y, dir_idx)

    # 현재 방향(상하좌우중)으로 주사위 움직이기
    new_top = top
    new_right = right
    new_front = front
    # 우
    if dir_idx == 0:
        new_top = 7 - right
        new_right = top
    # 하
    elif dir_idx == 1:
        new_top = 7 - front
        new_front = top
    # 좌
    elif dir_idx == 2:
        new_top = right
        new_right = 7 - top
    # 상
    else:
        new_top = front
        new_front = 7 - top


    top = new_top
    right = new_right
    front = new_front
    bottom = 7 - new_top
    # print("top", dir_idx, top, right)



def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def bfs():
    global cnt
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0

    visited[cur_x][cur_y] = 1
    while q:
        x, y = q.pop(0)
        # print(x, y)
        cnt += 1
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_range(nx, ny) and grid[nx][ny] == cur_num and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))

    # print(cnt, cur_num)


# 2. 좌판 점수 계산
def get_score():
    global cur_num
    # 현재 좌판 위치의 숫자와 같은 개수 상하좌우로 구하기 (bfs)
    cur_num = grid[cur_x][cur_y]
    q.append((cur_x, cur_y))
    bfs()

    # 개수로 점수 구하기
    return cnt * cur_num


# 3. 다음 방향 정하기
def select_dir():
    global dir_idx, cur_x, cur_y
    # 주사위 아랫면이 현재 칸의 수보다 크면 90도 시계방향 (+1)
    if cur_num < bottom:
        dir_idx += 1
        dir_idx = dir_idx % 4
    # // 작으면 90도 반시계 방향 (-1)
    elif cur_num > bottom:
        dir_idx -= 1
        if dir_idx < 0:
            dir_idx += 4
    #  동일하면 현재 방향으로 진행


    # print("bottom_num", bottom, cur_num)
    # print("dir_idx", dir_idx)


for i in range(m):
    # 1. 주사위 움직임
    move_dice()
    # 2. 좌판 점수 계산
    cnt = 0
    ans += get_score()
    # 3. 다음 방향 정하기
    select_dir()

print(ans)