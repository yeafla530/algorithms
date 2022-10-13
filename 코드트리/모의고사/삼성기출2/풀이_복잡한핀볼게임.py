EMPTY = -1
COLLISION = -2
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
undecided_pos = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 3]
marbles = [[EMPTY] * n for _ in range(n)]
next_marbles = [[EMPTY] * n for _ in range(n)]
temp = [[EMPTY] * n for _ in range(n)]

ans = 0
cur_score = 0


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def move(x, y, move_dir):
    global cur_score

    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    # 1번 블럭에서 방향 변환 0<->3  1<->2
    # 2번 블럭에서 방향 변환 0<->2  1<->3

    if grid[x][y] == 1:
        move_dir = 3 - move_dir
    elif grid[x][y] == 2:
        move_dir = (move_dir + 2) if move_dir < 2 else move_dir - 2

    nx, ny = x + dxs[move_dir], y + dys[move_dir]

    # 범위 안에 들어온다면 구슬 옮겨주기
    if in_range(nx, ny):
        if next_marbles[nx][ny] == EMPTY:
            next_marbles[nx][ny] = move_dir

        else:
            next_marbles[nx][ny] = COLLISION

    else:
        cur_score += 1


def move_all():
    for i in range(n):
        for j in range(n):
            if marbles[i][j] != EMPTY:
                move(i, j, marbles[i][j])


def remove_duplicates():
    for i in range(n):
        for j in range(n):
            if next_marbles[i][j] == COLLISION:
                next_marbles[i][j] = EMPTY


def simulate():
    # Step1. next_marble초기화
    for i in range(n):
        for j in range(n):
            next_marbles[i][j] = EMPTY

    # Step2. 구슬을 모두 한칸씩 이동시킨다
    move_all()

    # Step3. 구슬끼리 중복되는 경우 전부 제거한다
    remove_duplicates()

    # Step4. next_marbles결과를 marble로 옮겨준다
    for i in range(n):
        for j in range(n):
            marbles[i][j] = next_marbles[i][j]


def marble_exist():
    return any([
        marbles[i][j] != EMPTY
        for i in range(n)
        for j in range(n)
    ])


def get_score():
    global cur_score

    # Step1. 나중을 위해 초기 marble상태 저장
    for i in range(n):
        for j in range(n):
            temp[i][j] = marbles[i][j]

    # Step2. 구슬을 움직이는 시뮬 진행
    # 더이상 움직일 구슬이 없을때까지 반복
    cur_score = 0
    while marble_exist():
        simulate()

    # Step3. 초기 marble상태를 다시 복구 시켜준다
    for i in range(n):
        for j in range(n):
            marbles[i][j] = temp[i][j]

    return cur_score


def find_max(cnt):
    global ans

    if cnt == len(undecided_pos):
        ans = max(ans, get_score())
        return

    x, y = undecided_pos[cnt]

    for i in range(0, 3):
        grid[x][y] = i
        find_max(cnt + 1)
        grid[x][y] = 3


def input_marble(x, y, move_dir, marble_exist):
    if marble_exist:
        if marbles[x][y] == EMPTY:
            marbles[x][y] = move_dir

        else:
            marbles[x][y] = EMPTY


init_marbles = list(map(int, input().split()))
cnt = 0

# 초기 구슬상태
for j in range(n):
    input_marble(0, j, DOWN, init_marbles[cnt])
    cnt += 1

for i in range(n):
    input_marble(i, n - 1, LEFT, init_marbles[cnt])
    cnt += 1

for j in range(n - 1, -1, -1):
    input_marble(n - 1, j, UP, init_marbles[cnt])
    cnt += 1

for i in range(n - 1, -1, -1):
    input_marble(i, 0, RIGHT, init_marbles[cnt])
    cnt += 1

# 가능한 최대 구슬의 수 구하기
find_max(0)

print(ans)