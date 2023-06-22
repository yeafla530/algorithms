n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


dp = [[0 for _ in range(m)] for _ in range(n)]

def initial():
    dp[0][0] = grid[0][0]

    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    for i in range(1, m):
        dp[0][i] = dp[0][i - 1] + grid[0][i]

initial()

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = max(dp[i][j], dp[i-1][j-1] + grid[i][j])
        dp[i][j] = max(dp[i][j], dp[i][j-1] + grid[i][j])
        dp[i][j] = max(dp[i][j], dp[i-1][j] + grid[i][j])

print(dp[n-1][m-1])