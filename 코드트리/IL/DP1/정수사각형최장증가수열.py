n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
dp = [[1]*n for _ in range(n)]

# 포인트 : 칸 중 적혀있는 수가 작은 칸부터 오름차순 정렬해 그 순서대로 dp값 갱신
# 정렬한 이후 순서대로 dp값을 채우는 데 각 칸에 대해 4개 인접한 방향만 보면됨
cells = []
ans = 0

for i in range(n):
    for j in range(n):
        cells.append((a[i][j], i, j))

# 오름차순으로 정렬
cells.sort()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for _, x, y in cells:
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and a[nx][ny] > a[x][y]:
            dp[nx][ny] = max(dp[nx][ny], dp[x][y]+1)

for i in range(n):
    for j in range(n):
        ans = max(ans, dp[i][j])

print(ans)

# 230909 내 풀이 : 시간초과 (백트레킹 사용)
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]
visited = [[0]*n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def initial_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0


def step(i, j, x, y, cnt):
    for (dx, dy) in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if in_range(nx, ny) and not visited[nx][ny] and arr[x][y] >= arr[nx][ny]:
            dp[i][j] = max(dp[i][j], cnt)

        if in_range(nx, ny) and not visited[nx][ny] and arr[x][y] < arr[nx][ny]:
            visited[i][j] = 1
            step(i, j, nx, ny, cnt+1)
            visited[i][j] = 0


# 시작점
for i in range(n):
    for j in range(n):
        initial_visited()
        visited[i][j] = 1
        step(i, j, i, j, 1)

answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dp[i][j])

print(answer)


# 정답풀이

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

cells = []
ans = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


# 각 칸에 적혀있는 정수값 기준 오름차순이 되도록 칸의 위치 정렬
# (칸에 적힌 값, 행, 열) 순으로 넣어줌
for i in range(n):
    for j in range(n):
        cells.append((arr[i][j], i, j))

# 정렬
cells.sort()

def initial_visited():
    for i in range(n):
        for j in range(n):
            dp[i][j] = 1

print(cells)
# 정수값이 작은 칸부터 순서대로 보며 4방향에 대해 dp값 갱신
for _, x, y in cells:
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy 
        if in_range(nx, ny) and arr[nx][ny] > arr[x][y]:
            dp[nx][ny] = max(dp[nx][ny], dp[x][y] + 1)

    # for i in range(n):
    #     for j in range(n):
    #         print(dp[i][j], end=" ")
    #     print()
    # print()

for i in range(n):
    for j in range(n):
        ans = max(ans, dp[i][j])

print(ans)