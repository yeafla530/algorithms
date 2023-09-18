n = int(input())

grid = [[0]*n for _ in range(n)]
dp = [[0]*n for _ in range(n)]


for i in range(n):
    arr = list(map(int, input().split()))

    for j in range(len(arr)):
        grid[i][j] = arr[j]

dp[0][0] = grid[0][0]
for i in range(1, n):
    dp[0][i] = dp[0][i-1] + grid[0][i]
    dp[i][0] = dp[i-1][0] + grid[i][0]


for i in range(1, n):
    for j in range(1, n):
        if grid[i][j] == 0:
            continue
        
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]

ans = 0
for i in range(n):
    ans = max(dp[i][n-i-1], ans)

print(ans)