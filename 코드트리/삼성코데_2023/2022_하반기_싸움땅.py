EMPTY = (-1, -1, -1, -1, -1, -1)

n, m, k = map(int, input().split())
gun = [[[] for _ in range(n)] for _ in range(n)]
player = []

# 총
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        gun[i][j].append(arr[j])

# 플레이어
for i in range(m):
    x, y, d, s = map(int, input().split())
    player.append((i, x-1, y-1, d, s, 0))

points = [0] * m

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move(pos, d):
    ndir = d
    x, y = pos
    nx = x + dxs[d]
    ny = y + dys[d]

    # 범위를 벗어나면 반대 방향
    if not in_range(nx, ny):
        ndir = d+2 if d < 2 else d-2
        nx = x + dxs[ndir]
        ny = y + dys[ndir]

    return (nx, ny, ndir)

def find_player(pos):
    for i in range(m):
        num, x, y, d, s, a = player[i]
        # 같은 위치에 있는 플레이어 발견시
        if pos == (x, y):
            return player[i]
    return EMPTY
    # 발견 못하면 EMPTY

def update(p):
    num, _, _, _, _, _ = p
    player[num] = p


def get_gun(p):
    num, x, y, d, s, a = p
    
    gun[x][y].append(a)
    gun[x][y].sort(reverse=True)
    new_gun = gun[x][y][0]
    gun[x][y].pop(0)

    cur_player = (num, x, y, d, s, new_gun)
    update(cur_player)

def can_go(x, y):
    return in_range(x, y) and find_player((x, y)) == EMPTY


def loser(p):
    num, x, y, d, s, a = p

    # 총 버리기
    gun[x][y].append(a)
    loser = (num, x, y, d, s, 0)
    
    # 방향찾기
    for i in range(4):
        ndir = (d + i) % 4
        nx = x + dxs[ndir]
        ny = y + dys[ndir]

        if can_go(nx, ny):
            loser = (num, nx, ny, ndir, s, 0)
            get_gun(loser)
            break
        



def fight_player(p1, p2):
    num1, x1, y1, d1, s1, a1 = p1
    num2, x2, y2, d2, s2, a2 = p2

    hp1 = (s1 + a1, s1)
    hp2 = (s2 + a2, s2)


    if hp1 > hp2:
        points[num1] += (s1+a1) - (s2+a2)
        loser(p2)
        get_gun(p1)

    else:
        points[num2] += (s2+a2) - (s1+a1)
        loser(p1)
        get_gun(p2)



def simulate():
    # 모든 플레이어가 다 끝나야 1라운드 종료
    for i in range(m):
        num, x, y, d, s, a = player[i]
        # 한칸 이동 (방향과 위치가 바뀜)
        nx, ny, ndir = move((x, y), d)
        # 이 전 플레이어들 확인
        next_player = find_player((nx, ny))
        # 이동한 현재 플레이어
        cur_player = (num, nx, ny, ndir, s, a)
        # 이동한 플레이어 업데이트
        update(cur_player)

        # 플레이어를 찾지못했다면
        if next_player == EMPTY:
            get_gun(cur_player)            

        # 플레이어 찾았다면
        else:
            fight_player(cur_player, next_player)


for _ in range(k):
    simulate()


print(*points)