n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
# 폭탄 종류 표시
bomb_type = [[0]*n for _ in range(n)]
# 터진 곳 표시
bombed = [[0]*n for _ in range(n)]
dxs = [(1, 2, -1, -2), (1, 0, -1, 0), (1, 1, -1, -1)]
dys = [(0, 0, 0, 0), (0, -1, 0, 1), (-1, 1, 1, -1)]

max_cnt = 0
bomb_pos = []

def in_range(nx, ny):
    return 0 <= nx < n and 0 <= ny < n

def bomb(x, y, b_type):
    # 폭탄종류마다 터질위치 
    bombed[x][y] = 1
    
    for dx, dy in zip(dxs[b_type-1], dys[b_type-1]):
        nx = x + dx
        ny = y + dy
        if in_range(nx, ny):
            bombed[nx][ny] = 1
    


        


def calc():
    # Step1. 폭탄이 터진 위치를 표시하는 배열을 초기화
    for i in range(n):
        for j in range(n):
            bombed[i][j] = 0
    
    # 각 폭탄의 타입에 따라 초토화되는 영역 표시
    for i in range(n):
        for j in range(n):
            if bomb_type[i][j]:
                bomb(i, j, bomb_type[i][j])

    cnt = 0
    # 초토화된 영역의 수 구하기
    for i in range(n):
        cnt += sum(bombed[i][:])

    return cnt


def find_max_area(cnt):
    global max_cnt
    if cnt == len(bomb_pos):
        max_cnt = max(max_cnt, calc())
        return
    
    for i in range(1, 4):
        x, y = bomb_pos[cnt]

        bomb_type[x][y] = i
        find_max_area(cnt + 1)
        bomb_type[x][y] = 0

for i in range(n):
    for j in range(n):
        if grid[i][j]:
            bomb_pos.append((i, j))

find_max_area(0)
print(max_cnt)