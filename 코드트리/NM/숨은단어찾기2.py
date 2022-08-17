n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

# 왼쪽부터 시계방향
dxs = [0, -1, -1, -1, 0, 1, 1, 1]
dys = [-1, -1, 0, 1, 1, 1, 0, -1]


# 가로, 세로, 대각선에서 LEE를 찾는다
cnt = 0

def in_range(nx, ny, mx, my):
    return 0 <= nx < n and 0 <= ny < m and 0 <= mx < n and 0 <= my < m
for x in range(n):
    for y in range(m):
        for k in range(4):
            nx = x + dxs[k]
            ny = y + dys[k]

            mk = k+4
            mx = x + dxs[mk]
            my = y + dys[mk]
            # if in_range(nx, ny, mx, my):
            #     print(arr[nx][ny], arr[x][y], arr[mx][my])
            if in_range(nx, ny, mx, my) and ((arr[nx][ny] == "L" and arr[x][y] == "E" and arr[mx][my] == "E") or (arr[mx][my] == "L" and arr[x][y] == "E" and arr[nx][ny] == "E")):
                cnt += 1



print(cnt)