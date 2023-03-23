import sys

INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


dp = [
    [
        [INT_MAX] * (k+1)
        for _ in range(n)
    ]
    for _ in range(n)
]

dp[0][0][0] = INT_MIN
dp[0][0][1] = arr[0][0]

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            continue
        
        for l in range(k+1):
            # 왼쪽에서 오는 경우
            if j > 0:
                dp[i][j][l] = min(dp[i][j][l], dp[i][j-1][l])
            # 위에서 오는 경우
            if i > 0:
                dp[i][j][l] = min(dp[i][j][l], dp[i-1][j][l])
            
            # 현재 위치 색칠, 왼쪽에서 오는 경우
            if j > 0 and l > 0:
                dp[i][j][l] = min(dp[i][j][l], max(dp[i][j-1][l-1], arr[i][j]))
            
            # 현재위치 색칠, 위에서 오는 경우
            if i > 0 and l > 0:
                dp[i][j][l] = min(dp[i][j][l], max(dp[i-1][j][l-1], arr[i][j]))

print(dp[n-1][n-1][k])

