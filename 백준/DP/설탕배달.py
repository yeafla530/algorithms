n = int(input())

dp = [5001] * (n+1)
dp[0] = 0
sugar = [3, 5]

# 미리 채워놓기 
for x in sugar:
    for i in range(x, n+1):
        dp[i] = min(dp[i-x]+1, dp[i])

if dp[n] == 5001:
    print(-1)
else:
    print(dp[n])