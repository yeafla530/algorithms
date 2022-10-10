n, m, h, k = map(int, input().split())

# 도망자의 방향 저장
hiders = [[[] for _ in range(n)] for _ in range(n)]
next_hiders = [[[] for _ in range(n)] for _ in range(n)]
tree = [[False] * n for _ in range(n)]

# 정방향 기준으로 현재 위치에서 술래가 움직여야 할 방향 관리
seeker_next_dir = [[0] * n for _ in range(n)]
# 역방향 기준으로 현재 위치에서 술래가 움직여야 할 방향 관리
seeker_rev_dir = [[0] * n for _ in range(n)]

# 술래의 현재 위치
seeker_pos = (n // 2, n // 2)
# 술래가 움직이는 방향이 정방향이면 True, 아니면 False
forward_facing = True

ans = 0

# 술래 정보
for _ in range(m):
    x, y, d = map(int, input().split())
    hiders[x - 1][y - 1].append(d)

# 나무 정보
for _ in range(h):
    x, y = map(int, input().split())
    tree[x - 1][y - 1] = True

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]


def initialize_seeker_path():
    # 상우하좌

    cur_x, cur_y = seeker_pos
    # 이동 방향, 이동 횟수
    move_dir, move_num = 0, 1

    # 둘다 0, 0이면 멈춤
    while cur_x or cur_y:
        # move_num만큼 이동
        for _ in range(move_num):
            seeker_next_dir[cur_x][cur_y] = move_dir
            cur_x = cur_x + dxs[move_dir]
            cur_y = cur_y + dys[move_dir]
            seeker_rev_dir[cur_x][cur_y] = move_dir ^ 2

            # 이동하는 도중 (0, 0)으로 오게되면
            # 움직임 종료
            if not cur_x and not cur_y:
                break

        # 방향 바꿈
        move_dir = (move_dir + 1) % 4
        # 바뀐 값이 상 하면 1씩 증가
        if move_dir == 0 or move_dir == 2:
            move_num += 1


def dist_from_seeker(x, y):
    seeker_x, seeker_y = seeker_pos
    return abs(seeker_x - x) + abs(seeker_y - y)


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def hider_move(x, y, m_dir):
    nx, ny = x + dxs[m_dir], y + dys[m_dir]
    # Step1. 격자 벗어나면 방향 틀어줌
    if not in_range(nx, ny):
        m_dir ^= 2
        nx, ny = x + dxs[m_dir], y + dys[m_dir]

   # Step 2.
    # 그 다음 위치에 술래가 없다면 움직여줍니다.
    if (nx, ny) != seeker_pos:
        next_hiders[nx][ny].append(m_dir)
    # 술래가 있다면 더 움직이지 않습니다.
    else:
        next_hiders[x][y].append(m_dir)


# 술래 움직임
def hider_move_all():
    # Step1. next hider초기화
    for i in range(n):
        for j in range(n):
            next_hiders[i][j] = []

    # Step2. hider를 전부 움직여준다
    for i in range(n):
        for j in range(n):
            # 거리가 3 이내인 도망자들에 한해서
            if dist_from_seeker(i, j) <= 3:
                for m_dir in hiders[i][j]:
                    hider_move(i, j, m_dir)

            # 그렇지 않으면 현재 위치 그대로 넣어줌
            else:
                for m_dir in hiders[i][j]:
                    next_hiders[i][j].append(m_dir)

    # Step3. next hider값을 옮겨준다
    for i in range(n):
        for j in range(n):
            hiders[i][j] = next_hiders[i][j]


def get_seeker_dir():
    # 현재 술래의 위치 불러옴
    x, y = seeker_pos

    # 어느 방향으로 움직여야 하는지에 대한 정보 가져옴
    move_dir = 0
    if forward_facing:
        move_dir = seeker_next_dir[x][y]
    else:
        move_dir = seeker_rev_dir[x][y]

    return move_dir


def check_facing():
    global forward_facing

    # Case1 정방향으로 끝에 다다른 경우라면 방향을 바꿔줌
    if seeker_pos == (0, 0) and forward_facing:
        forward_facing = False

    # Case2. 역방향으로 끝에 다다른 경우여도 방향 바꿔줌
    if seeker_pos == (n // 2, n // 2) and not forward_facing:
        forward_facing = True


# 술래 이동
def seeker_move():
    global seeker_pos

    x, y = seeker_pos

    move_dir = get_seeker_dir()

    # 술래를 한칸 움직여둠
    seeker_pos = (x + dxs[move_dir], y + dys[move_dir])
    # 끝에 도달했다면 방향 바꿔줌
    check_facing()


# 점수를 얻는다
def get_score(t):
    global ans

    x, y = seeker_pos
    move_dir = get_seeker_dir()

    for dist in range(3):
        nx, ny = x + dist * dxs[move_dir], y + dist * dys[move_dir]

        # 범위안에 있고 나무가 없는 경우
        if in_range(nx, ny) and not tree[nx][ny]:
            ans += t * len(hiders[nx][ny])
            hiders[nx][ny] = []


def simulate(t):
    # 도망자가 움직인다
    hider_move_all()
    # 술래가 움직인다
    seeker_move()
    # 점수를 얻는다
    get_score(t)


# 술래잡기 시작전
# 술래 경로 정보 미리 계산
initialize_seeker_path()
for t in range(1, k + 1):
    simulate(t)

print(ans)