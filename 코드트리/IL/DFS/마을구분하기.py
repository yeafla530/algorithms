n = int(input())
villiage = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def dfs(x, y, cnt):
    for dx,dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if can_go(nx, ny):
            cnt += 1
    
    return cnt


dfs(0, 0, 0)