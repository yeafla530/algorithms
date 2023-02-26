# 내 풀이
n = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for x in range(n):
    for y in range(n):
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny]:
                cnt += 1
        
        if cnt >= 3:
            ans += 1

print(ans)


# 답
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

