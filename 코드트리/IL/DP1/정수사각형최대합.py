# dp 
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

def initial():
    dp[0][0] = grid[0][0]
    for i in range(1, n):
        dp[0][i] = dp[0][i-1] + grid[0][i]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + grid[i][0]

initial()
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])

print(dp[n-1][n-1])

# 230909
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]

def initial():
    dp[0][0] = arr[0][0]

    for i in range(1, n):
        dp[0][i] = dp[0][i-1] + arr[0][i]
        dp[i][0] = dp[i-1][0] + arr[i][0]


initial()


for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + arr[i][j]

print(dp[n-1][n-1])