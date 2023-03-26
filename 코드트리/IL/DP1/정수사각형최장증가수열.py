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