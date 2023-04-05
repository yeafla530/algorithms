from collections import deque
EMPTY = (-1, -1)
INT_MAX = 987654321

# n*n 칸, m명의 사람
n, m = map(int, input().split())
# 0이면 빈칸, 1이면 bc, 2면 아무도 갈 수 없는 곳
base_camp = [list(map(int, input().split())) for _ in range(n)]
# 편의점 목록
store = []


for _ in range(m):
    x, y = map(int, input().split())
    store.append((x-1, y-1))

# 사람들 위치 저장
player = [EMPTY] * m
cur_time = 0


dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]

# bfs에 사용되는 변수들 
# 최단거리 결과 기록 
step = [[0]*n for _ in range(n)]
visited = [[False]*n for _ in range(n)]



def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    return in_range(x, y) and base_camp[x][y] != 2 and not visited[x][y]


def bfs(pos):
    # 초기화
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
            step[i][j] = 0

    q = deque()
    q.append(pos)
    sx, sy = pos

    visited[sx][sy] = True
    step[sx][sy] = 0

    # BFS진행
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if can_go(nx, ny):
                visited[nx][ny] = True
                step[nx][ny] = step[x][y] + 1
                q.append((nx, ny))



def step1():
    # 편의점 향해 1칸 움직이기
    for i in range(m):
        if player[i] == EMPTY or player[i] == store[i]:
            continue

        # 편의점 위치에서 최단거리 찾기
        bfs(store[i])

        # 격자 안에 있다면 진행
        px, py = player[i]  

        # 현재 위치에서 상좌우하중 최단거리 값이 가장 작은 곳 고르기
        min_dist = INT_MAX
        min_x, min_y = -1, -1

        for dx, dy in zip(dxs, dys):
            nx, ny = px + dx, py + dy
            if in_range(nx, ny) and visited[nx][ny] and min_dist > step[nx][ny]:
                min_dist = step[nx][ny]
                min_x, min_y = nx, ny
    
        player[i] = (min_x, min_y)  


def step2():
    # 편의점에 도착한다면 해당 편의점에 멈춤
    for i in range(m):
        if player[i] == store[i]:
            px, py = player[i]
            base_camp[px][py] = 2
    # 사람들은 해당 편의점 지나갈 수 없음


def step3():
    global cur_time
    # 모든 사람들이 격자 안에 있지 않는 경우 bc으로 안감
    if cur_time > m:
        return
    
    # 3-1. 편의점으로부터 가장 가까운 베이스캠프 고르기 위해 편의점을 시작으로 하는 bfs시작
    bfs(store[cur_time-1])
    
    # 3-2. 편의점에서 가장 가까운 bc를 선택
    #       i, j가 증가하는 순으로 들리기 때문에 
    #       가장 가까운 bc가 여러개여도 알아서 (행, 열)순으로 골라짐
    min_dist = INT_MAX
    min_x, min_y = -1, -1
    for i in range(n):
        for j in range(n):
            # 방문 가능한 베이스 캠프 중 
            # 거리가 가장 가까운 위치 찾아주기
            if visited[i][j] and base_camp[i][j] == 1 and min_dist > step[i][j]:
                min_dist = step[i][j]
                min_x, min_y = i, j
        
    player[cur_time-1] = (min_x, min_y)
    base_camp[min_x][min_y] = 2

def end():
    # 단 한사람이라도 편의점에 도착하지 못하면 끝나지 않은 것
    for i in range(m):
        if player[i] != store[i]:
            return False
    return True 

def simulate():
    step1()

    step2()

    step3()

while True: 
    cur_time += 1
    simulate()

    if end():
        break

print(cur_time)