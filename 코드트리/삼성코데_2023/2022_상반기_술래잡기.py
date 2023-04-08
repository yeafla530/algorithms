# 술래
# 도망자 => 우좌 / 하상
# 나무 => 처음에 도망자와 겹치기 가능

# k번 반복
# 1. 도망자 이동
#    술래와 거리가 3이하인 도망자만 움직임 |x1-x2| + |y1-y2|
#    1. 바라보는 방향 격자 벗어나지 않을 때
#       1-1. 움직이려는 곳 술래있으면 이동안함
#       1-2. 술래 없으면 이동 나무가 있어도 괜찮
#    2. 격자 벗어날 때
#       2-1. 방향 반대로
#       2-2. 1칸 움직였을 때 술래 없으면 한칸 이동
#       2-3. 없으면 정지
# 2. 술래 이동
    # 달팽이 모양으로 이동 (시계방향)
    # 거꾸로 이동, 중심으로 이동
    # 중앙이나 맨 끝에 도달한 경우 방향 바로 반대로 틀어주기

# 3. 잡기
    # 바라보는 방향기준 3칸 
    # 나무가 놓인 칸은 도망자 안보임
    # t번째 턴 * 잡힌 도망자수 만큼 점수 얻음

n, m, h, k = map(int, input().split())
grid = [[[] for _ in range(n)] for _ in range(n)]
snail = [[0]*n for _ in range(n)]
players = []
for i in range(m):
    x, y, d = map(int, input().split())
    players.append((i, x-1, y-1, d-1, 0))
    grid[x-1][y-1].append((d-1, 0))

tree = [[False]*n for _ in range(n)]
for _ in range(h):
    tx, ty = map(int, input().split())
    tree[tx-1][ty-1] = True

# 정방향 기준으로
# 현재 위치에서 술래가 움직여야할 방향 관리
seeker_next_dir = [
    [0] * n
    for _ in range(n)
]

seeker_rev_dir = [[0]*n for _ in range(n)]
# 역방향기준
# 술래가 움직여야할 방향 관리

tagger = (n//2, n//2)
forward_facing = True

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n 


dirs = [[[0, 1], [0, -1]], [[1, 0], [-1, 0]]]



def initialize_seeker_path():
    dxs = [-1, 0, 1, 0]
    dys = [0, 1, 0, -1]

    curr_x, curr_y = n // 2, n // 2
    move_dir, move_num = 0, 1

    # 둘다 0, 0이면 멈춤
    while curr_x or curr_y:
        for _ in range(move_num):
            seeker_next_dir[curr_x][curr_y] = move_dir
            curr_x, curr_y = curr_x + dxs[move_dir], curr_y + dys[move_dir]
            # 다음 반대방향
            seeker_rev_dir[curr_x][curr_y] = move_dir + 2 if move_dir < 2 else move_dir - 2

            # 0, 0이면 종료
            if not curr_x and not curr_y:
                break
        
        move_dir = (move_dir + 1) % 4
        if move_dir == 0 or move_dir == 2:
            move_num += 1



def calc_distance_have_to_move(x, y, d, p):
    gx, gy = tagger

    if abs(x-gx) + abs(y-gy) <= 3:
        return True
    
    return False

def update(player):
    num, x, y, d, p = player

    for i in range(len(players)):
        if i == num:
            players[i] = player
            return
    
def reset_player():
    for i in range(n):
        for j in range(n):
            grid[i][j] = []

def player_move():
#    1. 술래와의 거리 계산 (3이하인 도망자만 이동)
    for i in range(len(players)):
        num, x, y, d, p = players[i]
        if calc_distance_have_to_move(x, y, d, p):
            nx, ny = x + dirs[d][p][0], y + dirs[d][p][1]
        #    1. 바라보는 방향 격자 벗어나지 않을 때
            if in_range(nx, ny):
        #       1-1. 움직이려는 곳 술래있으면 이동안함
                if (nx, ny) != tagger:   
        #       1-2. 술래 없으면 이동 나무가 있어도 괜찮
                    move_p = (num, nx, ny, d, p)
                    update(move_p)

        #    2. 격자 벗어날 때
            else:
        #       2-1. 방향 반대로
                np = (p+1)%2
        #       2-2. 1칸 움직였을 때 술래 없으면 한칸 이동
                nx, ny = x + dirs[d][np][0], y + dirs[d][np][1]
                if (nx, ny) != tagger:
                    move_p = (num, nx, ny, d, np)
                    update(move_p)
        #       2-3. 있으면 정지
                else:
                    move_p = (num, x, y, d, np)
                    update(move_p)


    reset_player()
    for i in range(len(players)):
        num, x, y, d, p = players[i]
        grid[x][y].append((d, p))



def get_seeker_dir():
    x, y = tagger

    move_dir = 0
    # 정방향이면
    if forward_facing:
        move_dir = seeker_next_dir[x][y] 
    # 정방향 아니면
    else:
        move_dir = seeker_rev_dir[x][y]
    
    return move_dir


def check_facing():
    # 끝에 도달했으면 방향 바꿔주기
    global forward_facing

    if tagger == (0,0) and forward_facing:  
        forward_facing = False
    if tagger == (n//2, n//2) and not forward_facing:
        forward_facing = True

# 상 우 하 좌
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def tagger_move():
    global tagger

    x, y = tagger
    move_dir = get_seeker_dir()

    tagger = (x + dxs[move_dir], y + dys[move_dir])

    check_facing()

def catch_player(t):
    global ans, players

    x, y = tagger
    move_dir = get_seeker_dir()

    for dist in range(3):
        nx, ny = x + dist * dxs[move_dir], y + dist * dys[move_dir]

        if in_range(nx, ny) and not tree[nx][ny] and len(grid[nx][ny]):
            ans += t * len(grid[nx][ny])
            grid[nx][ny] = []

   
    players = []
    num = 0
    for i in range(n):
        for j in range(n):
            if len(grid[i][j]):
                for k in range(len(grid[i][j])):
                    d, p = grid[i][j][k]
                    players.append((num, i, j, d, p))
                    num += 1


def simulate(t):
    # 1. 도망자 이동
    player_move()
    # 2. 술래 이동
    tagger_move()
    # 3. 도망자 잡기
    catch_player(t)


ans = 0
# 술래 경로 정보 미리 계산
initialize_seeker_path()

for t in range(1, k+1):
    simulate(t)

print(ans)