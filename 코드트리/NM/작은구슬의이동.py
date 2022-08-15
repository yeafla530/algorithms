n, t = map(int, input().split())
r, c, k = input().split()
r, c = int(r)-1, int(c)-1
d = {}
d['R'] = 0
d['D'] = 1
d['U'] = 2
d['L'] = 3

#서로 마주보도록
dxs = [0, 1, -1, 0]
dys = [1, 0, 0, -1]


cur_dir = d[k]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

for _ in range(t):
    nr, nc = r + dxs[cur_dir], c + dys[cur_dir]
    if in_range(nr, nc):
        r, c = nr, nc
    else:
        cur_dir = 3 - cur_dir

print(r+1, c+1)
    

## 강사님과 푼 풀이
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