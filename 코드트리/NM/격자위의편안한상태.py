n, m = map(int, input().split())
arr = [[0]*n for _ in range(n)]
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def adj_cnt(x, y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if in_range(nx, ny) and arr[nx][ny]:
            cnt += 1
    return cnt


for _ in range(m):
    r, c = map(int, input().split())
    r = r-1
    c = c-1

    arr[r][c] = 1
    if adj_cnt(r, c) == 3:
        print(1)
    else:
        print(0)


