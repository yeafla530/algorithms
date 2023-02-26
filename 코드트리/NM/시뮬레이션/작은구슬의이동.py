# 내 풀이
n, t = map(int, input().split())
r, c, d = input().split()
r = int(r)-1
c = int(c)-1

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

dir_num = {
    "U": 0,
    "R": 1,
    "L": 2,
    "D": 3
}

direct = dir_num[d]
for _ in range(t):
    r += dx[direct]
    c += dy[direct]
    # 한칸더 갔을 떄 범위를 벗어나지 않는다면
    if not(0 <= r < n and 0 <= c < n):
        direct = 3 - direct
        r += dx[direct]
        c += dy[direct]
     


print(r+1, c+1)


# 답
n, t = map(int, input().split())
x, y, c_dir = input().split()
x, y = int(x)-1, int(y)-1

mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

move_dir = mapper[c_dir]

dxs = [0, 1, -1, 0]
dys = [1, 0, 0, -1]

# 격자 위에 있는가
def in_range(x, y):
    return 0<=x<n and 0<=y<n

for _ in range(t):
    # 미리보기
    nx, ny = x + dxs[move_dir], y + dys[move_dir]

    # 격자 위에?
    if in_range(nx, ny):
        x, y = nx, ny
    
    # 벽에 부딪치면
    else:
        move_dir = 3 - move_dir

print(x+1, y+1)