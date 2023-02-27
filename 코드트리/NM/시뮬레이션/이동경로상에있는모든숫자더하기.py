n, t = map(int, input().split())
arr = list(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

dir_l = [3, 0, 1, 2]
dir_r = [1, 2, 3, 0]

mid = n//2
ans = grid[mid][mid]

x = mid
y = mid 
dir_num = 0


for i in range(t):
    if arr[i] == "R":
        dir_num = dir_r[dir_num]
    elif arr[i] == "L":
        dir_num = dir_l[dir_num]
    else:
        nx = x + dxs[dir_num]
        ny = y + dys[dir_num]
        if 0 <= nx < n and 0 <= ny < n:
            x = nx
            y = ny
            ans += grid[x][y]

print(ans)



