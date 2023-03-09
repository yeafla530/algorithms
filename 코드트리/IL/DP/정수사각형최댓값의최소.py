n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# 최대값을 최소로하는 경로
dp = [[0]*n for _ in range(n)]

def initial():
    dp[0][0] = arr[0][0]
    for i in range(1, n):
        dp[0][i] = max(dp[0][i-1], arr[0][i])
        dp[i][0] = max(dp[i-1][0], arr[i][0])

    
initial()

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(min(dp[i-1][j], dp[i][j-1]), arr[i][j])
    
print(dp[n-1][n-1])