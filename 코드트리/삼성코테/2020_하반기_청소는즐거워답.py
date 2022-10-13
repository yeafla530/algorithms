# 미리 방향마다 5*5 격자에 떨어지게 될 먼지의 비율을 담는 배열을 만든다
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

cur_x, cur_y = n // 2, n // 2
move_dir, move_num = 0, 1

ans = 0

dust_ratio = [
    [
        [0, 0, 2, 0, 0],
        [0, 10, 7, 1, 0],
        [5, 0, 0, 0, 0],
        [0, 10, 7, 1, 0],
        [0, 0, 2, 0, 0],
    ],
    [
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [2, 7, 0, 7, 2],
        [0, 10, 0, 10, 0],
        [0, 0, 5, 0, 0],
    ],
    [
        [0, 0, 2, 0, 0],
        [0, 1, 7, 10, 0],
        [0, 0, 0, 0, 5],
        [0, 1, 7, 10, 0],
        [0, 0, 2, 0, 0],
    ],
    [
        [0, 0, 5, 0, 0],
        [0, 10, 0, 10, 0],
        [2, 7, 0, 7, 2],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
    ]
]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def add_dust(x, y, dust):
    global ans
    if not in_range(x, y):
        ans += dust
    else:
        grid[x][y] += dust


def move():
    global cur_x, cur_y

    # 문제에서 원하는 진행 순서대로
    # 좌 하 우 상
    dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0]

    prev_x, prev_y = cur_x, cur_y
    cur_x, cur_y = cur_x + dxs[move_dir], cur_y + dys[move_dir]

    # 현재 위치 기준으로 각 위치에 먼지 더해줌
    added_dust = 0

    for i in range(5):
        for j in range(5):
            dust = grid[cur_x][cur_y] * dust_ratio[move_dir][i][j] // 100
            add_dust(cur_x + i - 2, cur_y + j - 2, dust)

            added_dust += dust

    # a%자리에 먼지 추가
    add_dust(cur_x + dxs[move_dir], cur_y + dys[move_dir], grid[cur_x][cur_y] - added_dust)


def end():
    return not cur_x and not cur_y


while not end():
    # move_num만큼 이동
    for _ in range(move_num):
        move()

        # (0, 0)오게 되면 종료
        if end():
            break

    move_dir = (move_dir + 1) % 4
    # 만약 현재 방향이 왼쪽 혹은 오른쪽이 된 경우
    if move_dir == 0 or move_dir == 2:
        move_num += 1

print(ans)
