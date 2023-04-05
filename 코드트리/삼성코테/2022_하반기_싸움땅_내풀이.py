EMPTY = (-1, -1, -1, -1, -1, -1)
# 총의 위치
# 플레이어


n, m, k = map(int, input().split())
gun = [[[] for _ in range(n)] for _ in range(n)]
player = []
points = [0] * m

for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        gun[i][j].append(arr[j])


for i in range(m):
    x, y, d, s = map(int, input().split())
    # x방향, y방향, 방향, 초기값, 총 공격력
    player.append((i, x-1, y-1, d, s, 0))


dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 플레이어 이동
def move(p):
    num, x, y, d, s, a = p

    nx = x + dxs[d] 
    ny = y + dys[d]

    if not in_range(nx, ny):
        d = (d+2) if d < 2 else (d - 2)
        nx = x + dxs[d]
        ny = y + dys[d]
    
    return nx, ny, d

def update(p):
    num, _, _, _, _, _ = p

    for i in range(m):
        num_i, _, _, _, _, _ = player[i]
        if num_i == num:
            player[i] = p
            break

# 총 얻기
def get_gun(p, pos):
    num, x, y, d, s, a = p
    gx, gy = pos

    
    gun[gx][gy].append(a)
    gun[gx][gy].sort(reverse=True)
    a = gun[gx][gy].pop(0)

    p = (num, gx, gy, d, s, a)
    update(p)
    


def in_player(idx, pos):
    for i in range(m):
        _, x, y, _, _, _ = player[i]
        if pos == (x, y):
            # print("사람있음")
            return player[i]
    return EMPTY

# 진 사람이 할 일
def loser(p):
    num, x, y, d, s, a = p
    
    # 총 내려놓기
    gun[x][y].append(a)

    for i in range(4):
        ndir = (d + i) % 4
        nx, ny = x + dxs[ndir], y + dys[ndir]
        if in_range(nx, ny) and in_player(num, (nx, ny)) == EMPTY:
            p = (num, nx, ny, ndir, s, 0)
            update(p)
            get_gun(p, (nx, ny))
            break





def fight(p1, p2):
    num1, x1, y1, d1, s1, a1 = p1
    num2, x2, y2, d2, s2, a2 = p2 

    hp1 = (s1+a1, s1)
    hp2 = (s2+a2, s2)

    if hp1 > hp2:
        points[num1] += (s1+a1) - (s2+a2)
        loser(p2)
        get_gun(p1, (x1, y1))

    else:
        points[num2] += (s2+a2) - (s1+a1)
        loser(p1)
        get_gun(p2, (x2, y2))





def simulate():
    for i in range(m):
        num, x, y, d, s, a = player[i]
        # 1. 플레이어 이동하기
        nx, ny, ndir = move(player[i])
        next_player = in_player(i, (nx, ny))
        cur_player = (num, nx, ny, ndir, s, a)
        update(cur_player)
        
        # 2. 플레이어 없는 경우
        if next_player == EMPTY:
            get_gun(cur_player, (nx, ny))
        #    2-1. 총이 있는 지 확인
        #       2-1-1. 총이 있으면 
        #              공격력이 쎈 총을 획득
        #              나머지 총 버리기

        else:
            fight(cur_player, next_player)
        #    2-2. 플레이어가 있으면 싸우기
        #         2-2-1. 플레이어 초기 능력치 + 총공격력 차이 (같으면 초기 공격력 높은 사람이 승리)
        #         2-2-2. 진 플레이어는 총을 격자에 내려놓고 원래 방향으로 한칸 이동
        #                만약 해당 칸에 플레이어 있거나 범위 밖이면 오른쪽 90도 회전애서 빈칸으로 이동
        #                총이 있다면 가장 공격력 높은 총 획득
        #         2-2-3. 이긴 플레이어는 승리한 칸에 떨어져있는 총과 원래있던 총 중 가장 공격력 높은 총 획득


for _ in range(k):
    simulate()

print(*points)