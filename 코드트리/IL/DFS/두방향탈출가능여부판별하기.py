n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dxs = [1, 0]
dys = [0, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def can_go(x, y):
    return in_range(x, y) and graph[x][y] and not visited[x][y]

def dfs(x, y):
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        # 갈 수 있는 길이라면
        if can_go(nx, ny):
            visited[nx][ny] = 1
            dfs(nx, ny)


# 초기값
visited[0][0] = 1
dfs(0, 0)
print(visited[n-1][m-1])