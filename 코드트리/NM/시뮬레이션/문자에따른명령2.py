arr = list(input())
# 동서남북
dx = [1,  0, -1, 0]
dy = [0, -1,  0, 1]
dir_num = 3

turn_r = [1, 2, 3, 0]
turn_l = [3, 0, 1, 2]

x, y = 0, 0
for direct in arr:
    # 시계반대
    if direct == 'L':
        # dir_num = (dir_num-1+4) % 4
        dir_num = turn_l[dir_num]
    # 시계
    elif direct == 'R':
        # dir_num = (dir_num+1) % 4
        dir_num = turn_r[dir_num]
    else:
        x = x + dx[dir_num]
        y = y + dy[dir_num]


print(x, y)

