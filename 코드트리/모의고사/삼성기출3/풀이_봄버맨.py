n = int(input())
grid = [
    input()
    for _ in range(n)
]

ans = 0


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def can_go(curr_x, curr_y, max_dist):
    # (x, y) 주위로 최대 max_dist 거리에 있는 몸을 이루고 있는
    # 모든 칸이 격자 안에 들어와야 하며, 벽이 아니어야만 합니다.

    # 이는 조건을 만족하는 칸의 개수가
    # (max_dist + 1) * (max_dist + 1) + max_dist * max_dist
    # 임을 확인하는 것으로 쉽게 판단이 가능합니다.
    cnt = 0

    for x in range(n):
        for y in range(n):
            if dist(curr_x, curr_y, x, y) <= max_dist and grid[x][y] != '#':
                cnt += 1

    return cnt == (max_dist + 1) * (max_dist + 1) + max_dist * max_dist


def find_max(curr_x, curr_y, step):
    global ans

    # 최대 턴 수를 갱신합니다.
    ans = max(ans, step)

    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    # 4 방향 중 한 곳으로 이동 후, 몸 크기를 키우는 것도
    # 문제없다면 그 다음 턴으로 넘어갑니다.
    for dx, dy in zip(dxs, dys):
        nx, ny = curr_x + dx, curr_y + dy

        # 해당 방향으로 이동 후 몸을 키우는게 가능하다면
        if can_go(nx, ny, step):
            find_max(nx, ny, step + 1)


start_x, start_y = -1, -1

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'B':
            start_x, start_y = i, j

find_max(start_x, start_y, 1)
print(ans)