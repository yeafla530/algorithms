n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# ㄱ자 블록, 1자블록
dxs = [(0, 1), (0, 1), (0, -1), (0, -1), (-1, 1), (0, 0)]
dys = [(-1, 0), (1, 0), (-1, 0), (1, 0), (0, 0), (-1, 1)]

def in_range(nx1, nx2, ny1, ny2):
    return 0 <= nx1 < n and 0 <= nx2 < n and 0 <= ny1 < m and 0 <= ny2 <m

max_num = 0
for x in range(n):
    for y in range(m):
        for (x1, x2), (y1, y2) in zip(dxs,dys):
            nx1 = x + x1
            nx2 = x + x2
            ny1 = y + y1
            ny2 = y + y2

            if in_range(nx1, nx2, ny1, ny2):
                # print(x, y)
                num = arr[x][y] + arr[nx1][ny1] + arr[nx2][ny2]
                max_num = max(max_num, num)

print(max_num)

