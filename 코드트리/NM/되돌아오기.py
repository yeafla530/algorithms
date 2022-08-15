n = int(input())
d = {
    'E': 0,
    'S': 1,
    'W': 2,
    'N': 3
}

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]


x, y = 0, 0
cur_dir = 0
t = 0
is_research = False
for _ in range(n):
    dis, a = input().split()
    a = int(a)
    cur_dir = d[dis]

    for _ in range(a):
        nx = x + dxs[cur_dir]
        ny = y + dys[cur_dir]

        x = nx
        y = ny
        t += 1
        

        if x == 0 and y == 0:
            is_research = True
            break
    if is_research:
        break
           
if is_research:
    print(t)
else:
    print(-1)
