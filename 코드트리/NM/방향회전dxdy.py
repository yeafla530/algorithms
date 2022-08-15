dir_num = 3 
x, y = 1, 5
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

# 시계방향
dir_num = (dir_num+1) % 4
# 반시계방향
dir_num = (dir_num-1+4) % 4

nx, ny = x + dx[dir_num], y + dy[dir_num]
