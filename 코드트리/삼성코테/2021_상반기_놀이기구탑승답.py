EMPTY = 0

n = int(input())
target_num = [0] * (n * n + 1)
friends = [[False] * (n * n + 1) for _ in range(n * n + 1)]
rides = [[0] * (n + 1) for _ in range(n + 1)]

dxs, dys = [-1, 1, 0, 0], [0, 0, 1, -1]


def in_range(x, y):
    return 1 <= x <= n and 1 <= y <= n


def is_friend(num1, num2):
    return friends[num1][num2]


def get_cur_call(num, x, y):
    friend_cnt, blank_cnt = 0, 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if not in_range(nx, ny):
            continue

        if rides[nx][ny] == EMPTY:
            blank_cnt += 1
        elif is_friend(num, rides[nx][ny]):
            friend_cnt += 1

    return (friend_cnt, blank_cnt, -x, -y)


def move(num):
    # 가장 우선순위가 높은 칸 선택
    # (좋친, 비어있는 칸, -행1, -열1)
    best_cell = (0, 0, -(n + 1), -(n + 1))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if rides[i][j] == EMPTY:
                curr = get_cur_call(num, i, j)

                if best_cell < curr:
                    best_cell = curr

    _, _, x, y = best_cell
    rides[-x][-y] = num


def get_score(x, y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and is_friend(rides[x][y], rides[nx][ny]):
            cnt += 1

    return int(10 ** (cnt - 1))


def get_total_score():
    return sum([
        get_score(i, j)
        for i in range(1, n + 1)
        for j in range(1, n + 1)
    ])


for i in range(1, n * n + 1):
    student_data = list(map(int, input().split()))
    target_num[i] = student_data[0]

    for friend_num in student_data[1:]:
        friends[target_num[i]][friend_num] = True

for i in range(1, n * n + 1):
    move(target_num[i])

ans = get_total_score()
print(ans)