import sys

INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize

# 변수 선언 및 입력:
n, k = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# dp[i][j][k]
# 시작 위치에서 잘 이동하여
# 정확히 k개의 칸에 색칠을 진행했고
# 현재 (i, j)에 위치에 서있을 때
# 색칠된 칸에 있는 수들 중 최댓값의 가능한 최솟값
# 가능한 최솟값을 구해야 하는 문제이므로
# 초기값은 INT_MAX가 되어야 합니다.
dp = [
    [
        [INT_MAX] * (k + 1)
        for _ in range(n)
    ]
    for _ in range(n)
]

# 초기 조건 : 시작 위치에 대한 설정
# 아직 색칠하지 않은 경우에는 최댓값 산정이 불가하므로 
# 최댓값을 구할 떄의 초기값인 INT_MIN을 적어줍니다.
dp[0][0][0] = INT_MIN 
# 첫 번째 칸에 색칠하는 경우
# grid[0][0]가 항상 최댓값이 됩니다.
dp[0][0][1] = grid[0][0]

# 점화식에 따라 값을 채워줍니다.
for i in range(n):
    for j in range(n):
        # 초기 조건에 대해서는 건너뜁니다.
        if i == 0 and j == 0:
            continue
        
        for l in range(k + 1):
            # Case 1. 현재 위치에 새로 색을 칠하지 않은 경우
            # Case 1 - 1. 왼쪽에서 오는 경우
            if j > 0:
                dp[i][j][l] = min(dp[i][j][l], dp[i][j - 1][l])
            # Case 1 - 2. 위에서 오는 경우
            if i > 0:
                dp[i][j][l] = min(dp[i][j][l], dp[i - 1][j][l])

            # Case 2. 현재 위치에 새로 색을 칠한 경우
            # Case 2 - 1. 왼쪽에서 오는 경우
            if j > 0 and l > 0:
                dp[i][j][l] = min(dp[i][j][l], 
                                  max(dp[i][j - 1][l - 1], grid[i][j])
                              )

            # Case 2 - 2. 위에서 오는 경우
            if i > 0 and l > 0:
                dp[i][j][l] = min(dp[i][j][l], 
                                  max(dp[i - 1][j][l - 1], grid[i][j])
                              )

print(dp[n - 1][n - 1][k])