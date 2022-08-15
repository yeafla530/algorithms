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

# 정답풀이
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
ans = -1
elapsed_time = 0

def move(move_dir, dist):
    global x, y
    global ans, elapsed_time

    for _ in range(dist):
        x, y = x + dxs[cur_dir], y + dys[cur_dir]
        elapsed_time += 1

        if x == 0 and y == 0:
            ans = elapsed_time 
            return True
    return False

for _ in range(n):
    dis, a = input().split()
    a = int(a)
    cur_dir = d[dis]


    done = move(dis, a)

    if done:
        break
           
print(ans)
