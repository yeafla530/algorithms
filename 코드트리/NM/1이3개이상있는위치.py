n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# 동서남북
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
ans = 0

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False  

def adjacent_cnt(x, y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and arr[nx][ny] == 1:
            cnt += 1
    return cnt

for x in range(n):
    for y in range(n):
        if adjacent_cnt(x, y) >= 3:
            ans += 1

print(ans)

