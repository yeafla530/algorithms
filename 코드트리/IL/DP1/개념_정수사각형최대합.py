import sys
INT_MIN = -sys.maxsize

n = 4
a = [
    [4],
    [6, 2],
    [3, 7, 9],
    [3, 4, 9, 9]
]

dp = [[0 for _ in range(4)] for _ in range(4)]


def initial():
    dp[0][0] = a[0][0]

    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + a[i][0]
    for i in range(1, n):
        dp[i][i] = dp[i-1][i-1] + a[i][i]

initial()

for i in range(2, n):
    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j] + a[i][j], dp[i-1][j-1] + a[i][j])

ans = INT_MIN
for j in range(n):
    ans = max(ans, dp[n-1][j])

print(ans)
