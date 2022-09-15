# 나 아주 칭찬해

import sys
max_num = -sys.maxsize

# 사각형 내 수들의 합이 최대 
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


def sum_num(x, y, i, j):
    num = 0
    # print(x, y, i, j)
    for a in range(x, x+i):
        for b in range(y, y+j):
            num += arr[a][b]
    # print(num)
    
    return num

# 사각형의 가로
for i in range(1, n+1):
    # 사각형의 세로
    for j in range(1, n+1):
        for x in range(n-i+1):
            for y in range(n-j+1):
                max_num = max(max_num, sum_num(x, y, i, j))

print(max_num)