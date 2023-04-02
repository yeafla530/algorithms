n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
bomb = []
visited = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            bomb.append((i, j))


pos1 = [(-2, 0), (-1, 0), (1, 0), (2, 0)]
pos2 = [(0, -1), (-1, 0), (1, 0), (0, 1)]
pos3 = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

pos = [pos1, pos2, pos3]
ans = 0



def in_range(x, y):
    return 0 <= x < n and 0 <= y < n 

def check_pos(num, cnt):
    loc = pos[num]
    x, y = bomb[cnt]
    
    for i in range(4):
        dx, dy = loc[i]
        if in_range(x+dx, y+dy) and grid[x+dx][y+dy] != 1:
            grid[x + dx][y + dy] += 2

def check_out(num, cnt):
    loc = pos[num]
    x, y = bomb[cnt]

    for i in range(4):
        dx, dy = loc[i]
        if in_range(x+dx, y+dy) and grid[x+dx][y+dy] != 1 :
            grid[x + dx][y + dy] -= 2


def count_bomb():
    count = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] >= 2:
                count += 1

    return count

def choose(cnt):
    global ans
    if cnt == len(bomb):
        ans = max(ans, count_bomb())
        # print(*grid, sep="\n")
        # print()
        return

    for i in range(3):
        check_pos(i, cnt)
        choose(cnt+1)
        check_out(i, cnt)


choose(0)
print(ans+len(bomb))