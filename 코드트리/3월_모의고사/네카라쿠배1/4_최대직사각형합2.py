n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 직사각형 크기 잡아주기
# (1~n)*(1~n)

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

ans = 0

for i in range(n):
    for j in range(n):
        # 시작점 : i, j
        for x in range(n):
            for y in range(n):
                if in_range(i+x, j+y):
                    sum_num = 0
                    for a in range(i, i+x+1):
                        for b in range(j, j+y+1):
                            sum_num += grid[a][b]
                    
                    ans = max(ans, sum_num)

print(ans)

# 풀이
import sys

INT_MIN = -sys.maxsize

# 변수 선언 및 입력:
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
ans = INT_MIN

def get_score(x1, y1, x2, y2):
    sum_val = 0
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            sum_val += grid[i][j]
    
    return sum_val
                               


# 모든 직사각형 잡아보는 완탐 진행
# 좌측 상단 모서리 i, j
# 우측 하단 모서리 k, l
for i in range(n):
    for j in range(n):
        for k in range(i, n):
            for l in range(j, n):
                ans = max(ans, get_score(i, j, k, l))

print(ans)