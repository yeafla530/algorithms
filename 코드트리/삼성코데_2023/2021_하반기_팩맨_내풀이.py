NUM_DIR = 8
PACK_DIR = 4
# 변수 선언 및 입력
n = 4
m, t = tuple(map(int, input().split()))

# 팩맨의 위치를 저장합니다.
px, py = tuple(map(int, input().split()))
px -= 1;
py -= 1

# [방향, 마리수]
monster = [[[0] * NUM_DIR for _ in range(n)] for _ in range(n)]
next_monster = [[[0] * NUM_DIR for _ in range(n)] for _ in range(n)]
dead = [[0] * n for _ in range(n)]
egg = [[[0] * NUM_DIR for _ in range(n)] for _ in range(n)]
# packman = [[0]*n for _ in range(n)]
# visited = [[0]*n for _ in range(n)]


dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, -1, -1, -1, 0, 1, 1, 1]

# 팩맨을 위한
# dx, dy를 따로 정의합니다.
# 우선순위에 맞춰
# 상좌하우 순으로 적어줍니다.
p_dxs = [-1, 0, 1, 0]
p_dys = [0, -1, 0, 1]


def copy_egg():
    # 같은 방향 가진 몬스터 복제 (알의 형태)
    for i in range(n):
        for j in range(n):
            for d in range(NUM_DIR):
                if monster[i][j][d] > 0:
                    egg[i][j][d] += monster[i][j][d]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def can_go(x, y):
    # 몬스터 시체가 있거나, 팩맨이 있는 경우거나 격자를 벗어나는 방향
    return in_range(x, y) and dead[x][y] == 0 and (x, y) != (px, py)


def find_next(x, y, d):
    nx, ny = 0, 0
    n_dir = d

    for i in range(NUM_DIR):
        n_dir = (d + i + NUM_DIR) % NUM_DIR
        nx, ny = x + dxs[n_dir], y + dys[n_dir]
        if can_go(nx, ny):
            return nx, ny, n_dir

    return x, y, d


def reset_next():
    for i in range(n):
        for j in range(n):
            for d in range(NUM_DIR):
                next_monster[i][j][d] = 0


def move_monster():
    reset_next()

    for i in range(n):
        for j in range(n):
            for d in range(NUM_DIR):
                # 몬스터가 있다면
                if monster[i][j][d] > 0:
                    # 갈 수 있는 방향 정하기
                    nx, ny, n_dir = find_next(i, j, d)
                    next_monster[nx][ny][n_dir] += monster[i][j][d]


    for i in range(n):
        for j in range(n):
            for d in range(NUM_DIR):
                monster[i][j][d] = next_monster[i][j][d]
    # 방향대로 한칸 이동
    # 몬스터 시체 있거나 팩맨 있는 경우, 격자 벗어나는 경우 반시계 45도 회전 한 후 판단
    # 갈 수 없다면


def collect_monster(x, y, z):
    arr = [x, y, z]
    visited = []
    count = 0
    cx, cy = px, py
    for i in range(3):
        d = arr[i]
        nx, ny = cx + p_dxs[d], cy + p_dys[d]
        if not in_range(nx, ny):
            return -1

        # 이미 방문한 곳을 갈 수 없는게 아니고
        # 방문한 곳은 다시 계산하지 않기!
        if (nx, ny) not in visited:
            count += sum(monster[nx][ny])
            visited.append((nx, ny))
        
        cx, cy = nx, ny

    return count


def move_packman():
    global px, py
    max_cnt = 0
    pack_dir = (0, 0, 0)
    for i in range(PACK_DIR):
        for j in range(PACK_DIR):
            for k in range(PACK_DIR):
                cnt = collect_monster(i, j, k)
                if max_cnt < cnt:
                    max_cnt = cnt
                    pack_dir = (i, j, k)

    for i in range(3):
        d = pack_dir[i]
        nx, ny = px + p_dxs[d], py + p_dys[d]

        for j in range(NUM_DIR):
            if monster[nx][ny][j] >= 1:
                monster[nx][ny][j] = 0
                dead[nx][ny] = 3

        px, py = nx, ny


def remove_dead():
    # 2턴 동안 유지
    for i in range(n):
        for j in range(n):
            if dead[i][j] > 0:
                dead[i][j] -= 1


def copy_monster():
    # 알 형태 몬스터 부화

    for i in range(n):
        for j in range(n):
            for d in range(NUM_DIR):
                monster[i][j][d] += egg[i][j][d]
                egg[i][j][d] = 0


def simulate():
    # 1. 몬스터 복제 => 매 초마다 기록하기 때문에 진행할 필요 없다 (?)
    copy_egg()
    # 2. 몬스터 이동
    move_monster()

    # 3. 팩맨 이동
    move_packman()
    # 4. 시체 소멸
    remove_dead()
    # 5. 몬스터 복제
    copy_monster()


for _ in range(m):
    mx, my, mdir = tuple(map(int, input().split()))
    # 첫번째 턴 (mx, my)위치의 방향 저장
    monster[mx - 1][my - 1][mdir - 1] += 1

for _ in range(t):
    simulate()

ans = 0
for i in range(n):
    for j in range(n):
        ans += sum(monster[i][j])

print(ans)