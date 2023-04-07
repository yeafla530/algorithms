# 내가 구해야할 것
# 1. 씨앗 => 위치, 성장 크기 (0은 새싹만 있는 곳)
# 2. 영양제 => 위치 오른쪽 => 반시계
# 3. 격자 => 각 끝과 끝이 연결되어있음 (반대편으로 돌아옴)
# 영양제 => 높이 1증가
# 씨앗만 있는 경우 높이 1의 리브로수 만듦

# 1. 특수 영양제 이동시킴
# 2. 특수 영양제 투입
# 3. 특수 영양제 투입한 리브로수의 대각선으로 인접한 방향에 1이상인 리브로수가 있는 만큼 성장
#    격자 벗어나는 경우 세지 않음

# 4. 특수 영양제 투입한 리브로수 제외하고 높이 2 이상인 리브로수는 높이 2를 베어 잘라낸 리브로수로 특수 영양제 사고 
#    해당 위치에 영양제 올려둠

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
grow = [[0]*n for _ in range(n)] # 성장하는 나무
drug = [[False]*n for _ in range(n)]
move_drug = [[False]*n for _ in range(n)]
position = []

for _ in range(m):
    d, p = map(int, input().split())
    position.append((d-1, p))


dxs = [0, -1, -1, -1, 0, 1, 1, 1]
dys = [1, 1, 0, -1, -1, -1, 0, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def initial():
    for i in range(n):
        for j in range(n):
            move_drug[i][j] = False

def move(d, p):
    initial()

    for i in range(n):
        for j in range(n):
            if drug[i][j]:
                nx = i + (dxs[d] * p)
                ny = j + (dys[d] * p)
                
                if not in_range(nx, ny):
                    if nx < 0:
                        nx = n + nx
                    elif nx >= n:
                        nx = nx - n
                    if ny < 0:
                        ny = n + ny
                    elif ny >= n:
                        ny = ny - n

                
                move_drug[nx][ny] = True

    for i in range(n):
        for j in range(n):
            drug[i][j] = move_drug[i][j]
            



def tree_grow():
    for i in range(n):
        for j in range(n):
            if drug[i][j]:
                grid[i][j] += 1

def find_initial():
    for i in range(n):
        for j in range(n):
            grow[i][j] = 0

axs = [-1, 1, -1, 1]
ays = [1, -1, -1, 1]
def find_tree():

    find_initial()

    for i in range(n):
        for j in range(n):
            if drug[i][j]:
                for ax, ay in zip(axs, ays):
                    nx = i + ax
                    ny = j + ay
                    if in_range(nx, ny) and grid[nx][ny]:
                        grow[i][j] += 1
    
    for i in range(n):
        for j in range(n):
            grid[i][j] += grow[i][j]

def remove_drug():
    for i in range(n):
        for j in range(n):
            drug[i][j] = False

def buy_drug():
    initial()

    for i in range(n):
        for j in range(n):
            if grid[i][j] >= 2 and not drug[i][j]:
                grid[i][j] -= 2
                move_drug[i][j] = True
    for i in range(n):
        for j in range(n):
            drug[i][j] = move_drug[i][j] 


def simulate(d, p):
    # 1. 영양제 이동시키기
    move(d, p)
    # 2. 영양제 투입 (나무 성장)
    tree_grow()
    # 3. 대각선 인접한 방향 1이상인 리브로수 성장
    find_tree()
    
    # 4. 특수 영양제 투입한 리브로수 제외
    #    높이 2이상인 리브로수 높이 2 베어 잘라내고
    #    영양제 올려둠 
    buy_drug()

# 초기 영양제 위치 설정
for i in range(n-2, n):
    for j in range(0, 2):
        drug[i][j] = True


ans = 0 # 남아있는 나무의 높이 합
# m년 반복
for i in range(m):
    d, p = position[i]
    simulate(d, p)

for i in range(n):
    for j in range(n):
        ans += grid[i][j]
print(ans)