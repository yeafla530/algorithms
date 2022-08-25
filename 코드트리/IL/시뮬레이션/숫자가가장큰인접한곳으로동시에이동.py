n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
count = [[0]*n for _ in range(n)]
next_count = [[0]*n for _ in range(n)]

for _ in range(m):
    r, c = map(int, input().split())
    count[r-1][c-1] = 1


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 상하 좌우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

# 다음 위치
def get_next_pos(x, y):
    max_num = 0
    pos = (x, y)
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if in_range(nx, ny) and grid[nx][ny] > max_num:
            max_num = grid[nx][ny]
            pos = (nx, ny)
    
    return pos


# count를 순환하면서 1인 곳 나오면 
def move_all():
    for i in range(n):
        for j in range(n):
            next_count[i][j] = 0
    
    for i in range(n):
        for j in range(n):
            if count[i][j] == 1:
                next_x, next_y = get_next_pos(i, j)
                next_count[next_x][next_y] += 1
    
    for i in range(n):
        for j in range(n):
            count[i][j] = next_count[i][j]

def remove():
    for i in range(n):
        for j in range(n):
            if count[i][j] >= 2:
                count[i][j] = 0


def simulate():
    # 움직인다
    move_all()
    # 2이상은 제거한다
    remove()

# t초동안 simulate 반복
for _ in range(t):
    simulate()

ans = 0
for i in range(n):
    for j in range(n):
        ans += count[i][j] 

print(ans)


#####이건 틀렸던 코드 
# 다시 분석해볼 필요
n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
count = [[0]*n for _ in range(n)]
next_count = [[0]*n for _ in range(n)]

for _ in range(m):
    r, c = map(int, input().split())
    count[r-1][c-1] = 1


#  가장 큰 값이 적혀있는 숫자가 있는 위치로 동시에 이동
def find_max(max_num, curr_max):
    if max_num < curr_max:
        max_num = curr_max
        return True
    return False


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 상하 좌우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

# 다음 위치
def get_next_pos(x, y):
    max_num = 0
    pos = (x, y)
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if in_range(nx, ny) and find_max(max_num, grid[nx][ny]):
            pos = (nx, ny)
    
    return pos


# count를 순환하면서 1인 곳 나오면 
def move_all():
    for i in range(n):
        for j in range(n):
            next_count[i][j] = 0
    
    for i in range(n):
        for j in range(n):
            if count[i][j] == 1:
                next_x, next_y = get_next_pos(i, j)
                next_count[next_x][next_y] += 1
    
    for i in range(n):
        for j in range(n):
            count[i][j] = next_count[i][j]

def remove():
    for i in range(n):
        for j in range(n):
            if count[i][j] >= 2:
                count[i][j] = 0


def simulate():
    # 움직인다
    move_all()
    # 2이상은 제거한다
    remove()

# t초동안 simulate 반복
for _ in range(t):
    simulate()

ans = 0
for i in range(n):
    for j in range(n):
        ans += count[i][j] 

print(ans)