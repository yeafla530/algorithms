# n: 미로 크기, m: 참가자수, k: 초수
######## 초기 세팅 ###########
n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
player = [[[] for _ in range(n)] for _ in range(n)]
player_loc = []
exit = []


for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    player_loc.append((x, y))
    print(x, y)
    player[x][y].append(1)
    

x, y = map(int, input().split())
exit.append(x)
exit.append(y)

grid[x-1][y-1] = -1 # 출구 표시
#############################
# 상 하 우 좌
dxs = [1, -1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_move(x, y):
    # 이동할 곳이
    # 벽이 없거나, 출구일경우
    if grid[x][y] == 0 and grid[x][y] == -1:
        return True
    else:
        return False


# 1. player 움직이기
def move():
    global sum_distance
    # 1. 동시에 움직임
    # 2. 벽이 없는 곳으로 이동가능
    # 3. 머물러있던 칸보다 출구까지 최단거리가 가까워야함
    # 4. 움직일 수 있는 칸이 2개이상이면 상하로 움직이는걸 우선시
    # 5. 참가자 움직일 수 없으면 안움직임
    # 6. 한칸에 2명이상 모험가 있을 수 있음
    
    # 한칸 이동
    move_dir = []
    for (x, y) in player_loc:
        min_loc = abs(x-exit[0]) + abs(y-exit[1])
        move_x, move_y = x, y

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if in_range(nx, ny) and can_move(nx, ny) and min_loc > (abs(nx-exit[0]) + abs(nx-exit[1])):
                move_x = nx
                move_y = ny

        sum_distance += abs(x-move_x) + abs(move_y)
        move_dir.append((move_x, move_y))

    for i in range(m):
        player_loc[i] = move_dir[i]
    


# 2. 미로 회전시키기
def rotate():
    # 한명 이상의 참가자와 출구 포함한 가장 작은 정사각형 잡는다
    # 가장 작은 크기를 갖는 정사각형이 2개 이상이라면, 좌상단 r좌표가 작은것이 우선
    # 같으면 c좌표가 작은것이 우선
    # 정사각형은 시계방향 90도 회전, 회전된 벽은 내구도 1씩 깎임
    pass


sum_distance = 0
last_exit = [0, 0]
# 초마다 실행되는 행동들
for _ in range(k):
    move() # 움직이기 
    rotate() # 회전하기

print(sum_distance)