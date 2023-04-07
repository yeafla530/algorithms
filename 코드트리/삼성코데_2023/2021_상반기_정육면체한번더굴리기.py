# 내가 정의할 것
# 주사위 정보 => 위치, 위 앞 옆, 방향
# 점수 => 숫자 * 개수
# 위치 => 처음엔 0, 0 / 오른쪽으로 움직임
# 회전 => 주사위 아랫면이 보드 해당칸에 있는 숫자보다 크면 현재 진행방향에서 90도 시계방향 회전
#         주사위 아랫면이 더 작으면 반시계 90도 회전
#         동일하면 현재 방향
from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
# 위, 앞, 옆
dice = [1, 2, 3]
next_dice = [0, 0, 0]
position = (0, 0)
# 우 하 좌 상
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir_num = 0


def slap_dice():
    for i in range(3):
        next_dice[i] = 0

    if dir_num == 0:
        next_dice[0] = 7-dice[2]
        next_dice[1] = dice[1]
        next_dice[2] = dice[0]

    elif dir_num == 1:
        next_dice[0] = 7-dice[1]
        next_dice[1] = dice[0]
        next_dice[2] = dice[2]

    elif dir_num == 2:
        next_dice[0] = dice[2]
        next_dice[1] = dice[1]
        next_dice[2] = 7-dice[0]
    
    else:
        next_dice[0] = dice[1]
        next_dice[1] = 7-dice[0]
        next_dice[2] = dice[2]

    for i in range(3):
        dice[i] = next_dice[i]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move(x, y):
    global position, dir_num
    # 이동하기
    nx = x + dirs[dir_num][0]
    ny = y + dirs[dir_num][1]

    if not in_range(nx, ny):
        dir_num = dir_num+2 if dir_num < 2 else dir_num-2
        nx = x + dirs[dir_num][0]
        ny = y + dirs[dir_num][1]

    position = (nx, ny)

    # 주사위 넘기기
    slap_dice()


def initial_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0

def bfs():
    initial_visited()
    q = deque()
    x, y = position
    q.append((x, y))
    visited[x][y] = 1
    count = 1

    while len(q):
        x, y = q.popleft()
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy

            if in_range(nx, ny) and not visited[nx][ny] and grid[x][y] == grid[nx][ny]:
                count += 1
                visited[nx][ny] = 1
                q.append((nx, ny))

    return count

def calc():
    global ans
    # 1. 이어져있는 같은 숫자 count
    cnt = bfs()
    # 2. 계산 
    x, y = position
    ans += grid[x][y] * cnt


def change_dir():
    global dir_num
    x, y = position
    down_num = 7-dice[0]
    grid_num = grid[x][y]

    if down_num > grid_num:
        dir_num = (dir_num+1) % 4
    elif down_num < grid_num:
        dir_num = (dir_num -1 + 4) % 4
    



def simulate():
    global position
    x, y = position
    # 1. 한칸 움직이기
    move(x, y)
    # 2. 점수 계산
    calc()
    # 3. 주사위 방향 결정
    change_dir()


ans = 0
for _ in range(m):
    simulate()

print(ans)