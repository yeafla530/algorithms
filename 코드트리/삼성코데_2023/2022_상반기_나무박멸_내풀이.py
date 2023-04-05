# 격자 크기, 박멸 진행되는 년수, 제초제 확산범위, 제초제 남아있는 년수
n, m, k, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
grow_tree = [[0]*n for _ in range(n)]
count_tree = [[0]*n for _ in range(n)]
potion = [[0]*n for _ in range(n)]

# 3. 나무가 가장 많이 박멸되는 칸에 제초제
#    나무가 있는 칸에 제초제 뿌리면 4개의 대각선 방향으로 k칸 만큼 전파하게 됨
#    전파 도중 벽이 있거나 나무가 아예 없는 칸은 그 칸까지만 뿌려지고 전파되지 않음
#    제초제가 뿌려진 칸에는 c년만큼 제추제 남아있다가 c+1년째 될 때 사라짐
#    다시 뿌려지는 경우 새로 뿌려진 해로부터 c년동안 유지됨
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
ans = 0
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def find_tree(x, y):
    count = 0
    for dx, dy in zip(dxs, dys):
        nx = x + dx 
        ny = y + dy

        if in_range(nx, ny) and grid[nx][ny] > 0 and potion[nx][ny] == 0:
            count += 1

    return count

def find_grow(x, y):
    count = 0
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if in_range(nx, ny) and grid[nx][ny] == 0 and potion[nx][ny] == 0:
            count += 1
    return count

def grow(x, y, num):
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if in_range(nx, ny) and grid[nx][ny] == 0 and potion[nx][ny] == 0:
            grow_tree[nx][ny] += num
    
    


# 1. 4개 칸중 나무가 있는 칸의 수만큼 나무 성장 (동시)
def step1():
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:
                grow = find_tree(i, j)
                grid[i][j] += grow


def step2():
    # 초기화
    for i in range(n):
        for j in range(n):
            grow_tree[i][j] = 0
# 2. 인접한 4개 칸 중 벽, 다른나무, 제초제 모두 없는 칸에 번식
#    이때 각 나무 그루 수에서 총 번식 가능한 칸의 개수만큼 나누어진 그루 수만큼 번식 진행 (동시)
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:
                count = find_grow(i, j)
                if count > 0:
                    num = grid[i][j] // count
                    grow(i, j, num)

     # 심기
    for i in range(n):
        for j in range(n):
            grid[i][j] += grow_tree[i][j]

axs = [-1, -1, 1, 1]
ays = [-1, 1, -1, 1]

def remove_count(x, y):
    count = grid[x][y]
    for ax, ay in zip(axs, ays):
        for n in range(1, k+1):
            nx = x + (ax * n)
            ny = y + (ay * n)
            
            if (not in_range(nx, ny)) or grid[nx][ny] <= 0:
                break

            count += grid[nx][ny]
    return count

def spread_potion(x, y):
    potion[x][y] = c
    grid[x][y] = 0
    for ax, ay in zip(axs, ays):
        for n in range(1, k+1):
            nx = x + (ax * n)
            ny = y + (ay * n)

            if not in_range(nx, ny) or grid[nx][ny] == -1: 
                break
            
            if grid[nx][ny] == 0:
                potion[nx][ny] = c

                break
            grid[nx][ny] = 0
            potion[nx][ny] = c



def step3():
    global ans
    # 뿌릴 때 1년 소모
    for i in range(n):
        for j in range(n):
            if potion[i][j] > 0:
                potion[i][j] -= 1
            

    max_x, max_y = -1, -1
    max_count = -1
    count = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:
                # 박멸할 나무 개수 세기
                count = remove_count(i, j)
                if max_count < count:
                    max_count = count
                    max_x, max_y = i, j
    # print(max_count)
    spread_potion(max_x, max_y)
    ans += max_count

def simulate():
    # 나무 성장시키기
    step1()
    print(*grid, sep="\n")
    print()
    
    # 번식
    step2()
    print(*grid, sep="\n")
    print()
    
    # 제초제
    step3()
    print(*potion, sep="\n")
    print()


for _ in range(m):
    simulate()


print(ans)