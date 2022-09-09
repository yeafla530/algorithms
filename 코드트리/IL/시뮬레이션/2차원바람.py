# 경계 숫자들을 시계방향으로 한칸씩 shift하고 
# 영역 내에 있는 값들을 각각 자신의 위치를 기준으로 자신과 인접한 원소들과의 평균값으로 바꿈

n, m, q = map(int, input().split())
a = [
    [0 for _ in range(m + 1)]
    for _ in range(n + 1)
]
temp_arr = [
    [0 for _ in range(m + 1)]
    for _ in range(n + 1)
]


def rotate(r1, c1, r2, c2):
    temp = a[r1][c1]

    for row in range(r1, r2):
        a[row][c1] = a[row+1][c1]
    
    for col in range(c1, c2):
        a[r2][col] = a[r2][col+1]
    
    for row in range(r2, r1, -1):
        a[row][c2] = a[row-1][c2]
    
    for col in range(c2, c1, -1):
        a[r1][col] = a[r1][col-1]
    
    a[r1][c1+1] = temp

def in_ranage(x, y):
    return 1 <= x <= n and 1 <= y <= m

def average(row, col):
    dxs = [0, 0, 1, 0, -1]
    dys = [0, 1, 0, -1, 0]
    num = 0
    n = 0
    for dx, dy in zip(dxs, dys):
        nx = row + dx
        ny = col + dy

        if in_ranage(nx, ny):
            num += a[nx][ny]
            n += 1
    return num // n

def set_average(r1, c1, r2, c2):
    for row in range(r1, r2+1):
        for col in range(c1, c2+1):
            temp_arr[row][col] = average(row, col)
    
    for row in range(r1, r2+1):
        for col in range(c1, c2+1):
            a[row][col] = temp_arr[row][col]


def simulate(r1, c1, r2, c2):
    # 직사각형 경계 숫자들 시계방향
    rotate(r1, c1, r2, c2)
    # 평균값 변경
    set_average(r1, c1, r2, c2)

# 초기화
for row in range(1, n+1):
    nums = list(map(int, input().split()))
    for col, num in enumerate(nums, start=1):
        a[row][col] = num

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())


    simulate(r1, c1, r2, c2)


for i in range(1, n+1):
    for j in range(1, m+1):
        print(a[i][j], end=" ")
    print()