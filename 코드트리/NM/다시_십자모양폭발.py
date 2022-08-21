n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
next_grid = [[0]*n for _ in range(n)]

def in_bomb_range(x, y, center_x, center_y, bomb_range):
    # x, y 축 같고 거리가 bomb_range보다 작으면
    return (x == center_x or y == center_y) and abs(x - center_x) + abs(y - center_y) < bomb_range

def bomb(center_x, center_y):
    bomb_range = grid[center_x][center_y]
    
    # 폭탄이 터질위치는 0으로 채워준다
    for i in range(n):
        for j in range(n):
            if in_bomb_range(i, j, center_x, center_y, bomb_range):
                grid[i][j] = 0

    # 위에서 아래로, 열 고정 
    for j in range(n):
        next_row = n - 1
        for i in range(n-1, -1, -1):
            # grid값이 있으면 
            if grid[i][j]:
                next_grid[next_row][j] = grid[i][j]
                next_row -= 1

    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]


        



r, c = map(int, input().split())
bomb(r-1, c-1)


for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()