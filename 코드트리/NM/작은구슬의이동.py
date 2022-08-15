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
    

