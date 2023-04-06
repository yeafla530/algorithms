from collections import deque

EMPTY = (-1, -1)
INT_MAX = 987654321

n, m = map(int, input().split())
# 0 : 비어있음, 1 : 베이스 캠프, 2 : 못감
grid = [list(map(int, input().split())) for _ in range(n)]
store = []

for i in range(m):
    x, y = map(int, input().split())
    store.append((x-1, y-1))


people = [EMPTY] * m
step = [[0]*n for _ in range(n)]
visited = [[0]*n for _ in range(n)]
dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def reset():
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0
            step[i][j] = 0


def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and grid[x][y] != 2

def bfs(q):
    while len(q):
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = 1
                step[nx][ny] = step[x][y] + 1
# 격자에 있는 사람 움직이기

def step1():
    # 본인이 가고싶은 편의점 방향 향해서 이동
    # 격자 안에 없으면 이동 x
    for i in range(m):
        x, y = store[i]
        if people[i] == EMPTY or people[i] == (x, y):
            continue
        
        reset()
        q = deque()
        q.append((x, y))
        visited[x][y] = 1

        bfs(q)

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


# 편의점에 도달하면 멈춤
def step2():
    for i in range(m):
        x, y = store[i]
        px, py = people[i]

        if (x, y) == (px, py):
            grid[px][py] = 2
    

def find_basecamp(idx):
    min_x, min_y = -1, -1
    min_num = INT_MAX
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1 and visited[i][j] and min_num > step[i][j]:
                min_x, min_y = i, j

                min_num = step[i][j]

    grid[min_x][min_y] = 2
    people[idx] = (min_x, min_y)


                


def step3():
    global cur_time
    if cur_time > m:
        return
    
    # 가장 가까이에 있는 편의점 가기
    reset()

    x, y = store[cur_time-1]
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    
    # 최단거리 표시
    bfs(q)

    find_basecamp(cur_time-1)

    # print(people)


def simulate():
    step1()
    step2()
    step3()


def end():
    # 모든 사람이 편의점에 있으면 종료
    for i in range(m):
        x, y = store[i]
        px, py = people[i]

        if (x, y) != (px, py):
            return False

    return True
        


cur_time=  0
# 모든 사람이 편의점에 도달할때까지 진행 
while True:
    cur_time += 1
    simulate()

    if end():
        break

print(cur_time)