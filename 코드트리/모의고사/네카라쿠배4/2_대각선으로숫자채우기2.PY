# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
grid = [
    [0] * m
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

   
# 수들을 채워봅니다. 
# 라인 수만큼 채워줍니다.
num = 1
for line_num in range(1, n + m):
    # 홀수번째 라인이라면
    # 우측 상단으로 계속 올라가며 채워줍니다.
    # 이때 시작 위치는 일반적으로
    # (n - 1, line_num - n) 가 됩니다.
    if line_num % 2 == 1:
        i, j = n - 1, line_num - n
        while i >= 0:
            # 범위 안에 들어온다면
            # 해당 위치에 수를 적어줍니다.
            if in_range(i, j):
                grid[i][j] = num
                num += 1
            # 우측 상단으로 움직입니다.
            i -= 1 
            j += 1
    # 짝수번째 라인이라면
    # 좌측 하단으로 계속 내려가며 채워줍니다.
    # 이때 시작 위치는 일반적으로
    # (0, line_num - 1)이 됩니다.
    else:
        i, j = 0, line_num - 1
        while i < n:
            # 범위 안에 들어온다면
            # 해당 위치에 수를 적어줍니다.
            if in_range(i, j):
                grid[i][j] = num
                num += 1
            # 좌측 하단으로 움직입니다.
            i += 1 
            j -= 1

# 답을 출력합니다.
for i in range(n):
    for j in range(m):
        print(grid[i][j], end=" ")
    print()