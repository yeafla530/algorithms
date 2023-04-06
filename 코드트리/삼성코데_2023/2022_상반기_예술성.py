# 색깔별 그룹
# 예술점수 = (a 칸수 + b칸수) * a 숫자 * b숫자값 * 맞닿은 변 수 

# 모든 그룹의 예술점수 합 = 초기 예술점수
# 1. 회전 진행 => 정중앙 기준선 만듦
#    10자 모양 반시계 90도회전
#    4개의 사각형 개발 시계방향 90도

# 2. 회전 후 전체 예술점수 구하기 

# 총 3최전 이후의 예쑬점수 합 구하기
from collections import deque


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
group = [[0]*n for _ in range(n)]
visited = [[0]*n for _ in range(n)]
colors = [0] + []
rotate_temp = [[0]*n for _ in range(n)]


dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def bfs(x, y, grou_num):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    group[x][y] = grou_num
    count = 1

    while len(q):
        x, y = q.popleft()
        num = grid[x][y]
        group[x][y] = grou_num

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            
            if in_range(nx, ny) and not visited[nx][ny] and num == grid[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
                count += 1
    
    colors.append(count)



def reset_visit():
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0
            group[i][j] = 0


axs = [1, 0]
ays = [0, 1]

def calc_block():
    num = 0
    for x in range(n):
        for y in range(n):
            for ax, ay in zip(axs, ays):
                nx = x + ax
                ny = y + ay

                if in_range(nx, ny) and group[x][y] != group[nx][ny]:
                    bn, tn = group[x][y], group[nx][ny] 
                    num1, num2 = grid[x][y], grid[nx][ny]
                    cnt1, cnt2 = colors[bn], colors[tn] # 컬러개수
                    num += (cnt1 + cnt2) * num1 * num2

    return num




def calc():
    global ans, colors

    reset_visit()
    group_num = 0
    a = 0
    colors = [0] + []
    # print(colors)
    # 붙어있는 색깔의 수 구하기
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                group_num += 1
                bfs(i, j, group_num)
    

    # 점수 계산하기
    ans += calc_block() 


def reset_temp():
    for i in range(n):
        for j in range(n):
            temp[i][j] = 0 



def right_rotate(copy_grid, length):
    temp = list(map(list, zip(*copy_grid[::-1])))

    for i in range(length):
        for j in range(length):
            copy_grid[i][j] = temp[i][j]

    

def line_rotate():
    idx = n // 2

    copy_grid = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            copy_grid[i][j] = grid[i][j]

    for _ in range(3):
        right_rotate(copy_grid, n)

    for i in range(n):
        rotate_temp[i][idx] = copy_grid[i][idx]
        rotate_temp[idx][i] = copy_grid[idx][i]
    


def part_rotate(sx, sy, s):
    copy_grid = [[0]*s for _ in range(s)]

    for x in range(sx, sx+s):
        for y in range(sy, sy+s):
            ox, oy = x - sx, y - sy
            copy_grid[ox][oy] = grid[x][y]
    right_rotate(copy_grid, s)
    

    for x in range(sx, sx+s):
        for y in range(sy, sy+s):
            ox, oy = x-sx, y-sy
            rotate_temp[x][y] = copy_grid[ox][oy]




# 회전하기
def rotate():
    # 1. 십자 회전
    line_rotate()

    # 2. 부분 회전
    
    # x의 시작점, y의 시작점, 길이
    part_rotate(0, 0, n//2)
    part_rotate(0, n//2+1, n//2)
    part_rotate(n//2+1, 0, n//2)
    part_rotate(n//2+1, n//2+1, n//2)

    # print("rotate_temp", rotate_temp)
    for i in range(n):
        for j in range(n):
            grid[i][j] = rotate_temp[i][j]


def simulate():
    rotate()
    calc()

ans = 0
# 초기 예술점수 구하기
calc()
# 회전 후 점수 구하기
for i in range(3):
    simulate()
    
print(ans)