from collections import deque

INT_MAX = 987654321
EMPTY = (-1, -1)

n, m = map(int, input().split())
# 빈칸 0, 베이스 캠프 1, 갈 수 없는 칸 2
grid = [list(map(int, input().split())) for _ in range(n)]
store= []

# 편의점 위치
for _ in range(m):
    x, y = map(int, input().split())
    store.append((x-1, y-1))

# 얼마나 나아가야하는지 기록
step = [[0]*n for _ in range(n)]
visited = [[False]*n for _ in range(n)]
# 사람들 위치 표시
people = [EMPTY] * m


dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 < y <= n


def can_go(x, y):
    # 범위 안에 있고, 갈 수 있는 곳이며, 방문하지 않은 곳

    return in_range(x, y) and not visited[x][y] and grid[x][y] != 2

def bfs(pos):
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0
            step[i][j] = 0
    
    px, py = pos
    q = deque()
    q.append(pos)
    visited[px][py] = True

    # 편의점으로부터 최단거리 구함
    while len(q):
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True
                step[nx][ny] = step[x][y] + 1
    



def step1():
    # 격자에 있는 사람들이 1칸 씩 이동
    for i in range(m):
        if people[i] == EMPTY or people[i] == store[i]:
            continue
        # 편의점 위치에서 최단거리 구하기 
        bfs(store[i])
        # print(step)

        px, py = people[i]
        min_x, min_y = -1, -1
        min_num = INT_MAX

        for dx, dy in zip(dxs, dys):
            nx = px + dx
            ny = py + dy

            if in_range(nx, ny) and visited[nx][ny] and min_num > step[nx][ny]:
                min_x, min_y = nx, ny
                min_num = step[nx][ny]
        
        people[i] = (min_x, min_y)

    # 상좌우하 우선순위로 움직임
    # 최단거리라 하면 최소가 되는 거리


def step2():
    # 편의점 도착하면 해당 편의점에 멈추고
    # 다른 사람들은 편의점 못지나감
    for i in range(m):
        if people[i] == store[i]:
            x, y = people[i]
            grid[x][y] = 2


def step3():
    # 현재 시간 t분이고 t <= m이면 베이스 캠프로
    # 아닌 경우엔 그냥 패스 
    # 이 베이스 캠프는 다른 사람이 못지나감
    if curr_time > m:
        return
    
    # 0-2번째 편의점에서 베이스 캠프 최단 거리 구하기
    bfs(store[curr_time-1]) 

    sx, sy = -1, -1
    min_num = INT_MAX

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1 and visited[i][j] and min_num > step[i][j]:
                min_num = step[i][j]
                sx, sy = i, j
    
    people[curr_time-1] = (sx, sy)
    people[min_x][min_y] = 2



def simulate():
    step1()

    step2()

    step3()



def end():
    for i in range(m):
        if people[i] != store[i]:
            return False
    return True 

curr_time = 0
while True:
    curr_time += 1
    simulate()

    if end():
        break

print(curr_time)