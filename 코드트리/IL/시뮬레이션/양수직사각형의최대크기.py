# 직사각형 내부 전부 양수
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]


def get_max_size(x1, y1, x2, y2):
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            if a[i][j] <= 0:
                return -1
    return abs(x1-(x2+1)) * abs(y1-(y2+1))

# 직사각형 중 최대 크기 
max_size = -1
for i in range(n):
    for j in range(m):
        for k in range(i, n):
            for l in range(j, m):
                max_size = max(max_size, get_max_size(i, j, k, l))
                # print(max_size)

print(max_size)