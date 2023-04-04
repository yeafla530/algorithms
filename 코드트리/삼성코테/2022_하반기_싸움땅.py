EMPTY = (-1, -1, -1, -1, -1, -1)

n, m, k = map(int, input().split())
gun = [[[] for _ in range(n)] for _ in range(n)]

# 총이 놓인 칸
for i in range(n):
    nums = list(map(int, input().split()))
    for j in range(n):
        if nums[j] != 0:
            gun[i][j].append(nums[j])

# 사람들 위치
players = []

# 위 오른쪽 아래 왼쪽
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

# 위치, 초기 능력치 설정
for i in range(m):
    x, y, d, s = map(int, input().split())
    # 번호, x, y, 방향, 초기능력, 총 데미지
    players.append((i, x-1, y-1, d, s, 0))

# 포인트
points = [0] * m

# 격자 내부
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def find_player(pos):
    for i in range(m):
        _, x, y, _, _, _ = players[i]
        if pos == (x, y):
            return players[i]

    return EMPTY        

# 플레이어 움직이고 총 얻기
def move_get_gun(p, pos):
    num, x, y, d, s, a = p
    nx, ny = pos
    # print(x, nx, y, ny)

    # 가장 좋은 총으로 갱신
    gun[nx][ny].append(a)
    gun[nx][ny].sort(reverse=True)
    a = gun[nx][ny][0]
    gun[nx][ny].pop(0)

    # 총 업데이트
    p = (num, nx, ny, d, s, a)
    update(p)


# 플레이어 업데이트
def update(p):
    num, _, _, _, _, _ = p
    for i in range(m):
        num_i, _, _, _, _, _ = players[i]

        if num_i == num:
            players[i] = p
            break

# 다음 스텝
def get_next(x, y, d):
    nx, ny = x + dxs[d], y + dys[d]
    # 격자 안에 없으면
    if not in_range(nx, ny):
        # 정반대방향으로 회전
        d = (d + 2) if d < 2 else (d-2)
        nx, ny = x + dxs[d], y + dys[d]
    
    return (nx, ny, d)

def loser_move(p):
    num, x, y, d, s, a = p
    # 가지고 있는 총 내려놓기
    gun[x][y].append(a)
    # 원래 가지고 있던 방향대로 한칸 이동
    # 다른 플레이어 있거나 격자 밖인 경우 오른쪽 90도 회전
    # 해당 칸에 총이 있으면 가장 공격력 높은 총 획득하고 나머지 총 격자에 내려놓음
    for i in range(4):
        # 오른쪽 90도 회전
        ndir = (d + i) % 4
        nx, ny = x + dxs[ndir], y + dys[ndir]
        if in_range(nx, ny) and find_player((nx, ny)) == EMPTY:
            p = (num, x, y, ndir, s, 0)
            move_get_gun(p, (nx, ny))
            break


def duel(p1, p2, pos):
    num1, _, _, d1, s1, a1 = p1
    num2, _, _, d2, s2, a2 = p2

    # (초기 능력치 + 총 공격력, 초기 능력치) 순으로 우선순위 매겨 비교

    # p1이 이긴경우 (같은 경우엔 초기값을 기준으로 우선순위가 정해짐)
    if (s1 + a1, s1) > (s2 + a2, s2):
        # point얻기
        points[num1] += (s1+a1) - (s2+a2)
        # p2 진사람 움직이기
        loser_move(p2)
        # p1 이긴사람 움직이기 
        move_get_gun(p1, pos)

    # p2가 이긴 경우
    else:
        points[num2] += (s2+a2) - (s1+a1)
        loser_move(p1)
        move_get_gun(p2, pos)




# 1라운드 진행
def simulate():
    # 첫번째 플레이어부터 순서대로 진행 
    for i in range(m):
        num, x, y, d, s, a = players[i]

        # Step1-1. 현재 플레이어가 움직일 그 다음 위치와 방향 구하기
        nx, ny, ndir = get_next(x, y, d)

        # 해당 위치에 있는 전 플레이어 정보 얻어오기 (있는지 없는지 확인 )
        next_player = find_player((nx, ny))

        # 현재 플레이어 위치와 방향 보정
        curr_player = (num, nx, ny, ndir, s, a)
        update(curr_player)

        # Step2 해당 위치로 이동해본다
        # Step2-1. 해당 위치에 플레이어가 없다면 그대로 움직이기
        if next_player == EMPTY:
            move_get_gun(curr_player, (nx, ny))
        # Step2-2. 해당 위치에 플레이어가 있다면 결투 진행
        else:
            duel(curr_player, next_player, (nx, ny))

# k번 반복
for _ in range(k):
    simulate()


print(*points)