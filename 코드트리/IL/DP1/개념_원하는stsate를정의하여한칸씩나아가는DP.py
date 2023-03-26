import sys
INT_MIN = -sys.maxsize

n = 2
a = [0, 2, 4, 1, 6]
dp = [
    [0 for _ in range(2 * n +1)]
    for _ in range(2 * n +1)
]

def initialize():
    for i in range(2 * n + 1):
        for j in range(2 * n + 1):
            dp[i][j] = INT_MIN
    dp[0][0] = 0

initialize()

for i in range(1, 2*n+1):
    dp[i][0] = dp[i-1][0]
    for j in range(1, i+1):
        if j % 2 == 1:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + a[i])
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] - a[i])

print(dp[2*n][n])