n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
drugs = [[0] * n for _ in range(n)]

# 오른쪽부터 반시계
dxs = [0, -1, -1, -1, 0, 1, 1, 1]
dys = [1, 1, 0, -1, -1, -1, 0, 1]
for i in range(n - 1, n - 3, -1):
    for j in range(0, 2):
        drugs[i][j] = 1

next_drugs = [[0] * n for _ in range(n)]


def move(x, y):
    nx = x + (dxs[d] * p)
    ny = y + (dys[d] * p)

    if nx < 0:
        nx = n + nx
    elif nx >= n:
        nx = nx - n

    if ny < 0:
        ny = n + ny
    elif ny >= n:
        ny = ny - n

    next_drugs[nx][ny] = 1


# 영양제 이동
def move_drug(d, p):
    for i in range(n):
        for j in range(n):
            next_drugs[i][j] = 0

    for i in range(n):
        for j in range(n):
            if drugs[i][j]:
                move(i, j)

    for i in range(n):
        for j in range(n):
            drugs[i][j] = next_drugs[i][j]


def put_drug():
    for i in range(n):
        for j in range(n):
            if drugs[i][j]:
                grid[i][j] += 1


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


add_tree = [[0] * n for _ in range(n)]


def grow_tree():
    nxs = [-1, -1, 1, 1]
    nys = [-1, 1, 1, -1]
    for i in range(n):
        for j in range(n):
            add_tree[i][j] = 0

    for i in range(n):
        for j in range(n):
            if drugs[i][j]:
                for dx, dy in zip(nxs, nys):
                    nx = i + dx
                    ny = j + dy

                    if in_range(nx, ny):
                        if grid[nx][ny] >= 1:
                            add_tree[i][j] += 1

    for i in range(n):
        for j in range(n):
            grid[i][j] += add_tree[i][j]

    # print(grid)


def cut_tree():
    for i in range(n):
        for j in range(n):
            next_drugs[i][j] = 0

    for i in range(n):
        for j in range(n):
            if grid[i][j] >= 2 and not drugs[i][j]:
                grid[i][j] -= 2
                next_drugs[i][j] = 1

    for i in range(n):
        for j in range(n):
            drugs[i][j] = next_drugs[i][j]


# 년수
for _ in range(m):
    d, p = map(int, input().split())
    d -= 1

    # 1. 영양제 이동
    move_drug(d, p)
    # 2. 영양제 투입
    put_drug()
    # 3. 나무 높이 성장시키기
    grow_tree()

    # 4. 영양제 투입 제외, 2이상인 나무 체크해서 높이 -2 후 영양제 올려놓기
    cut_tree()

result = 0
for i in range(n):
    for j in range(n):
        result += grid[i][j]

print(result)