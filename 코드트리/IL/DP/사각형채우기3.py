# 너무 어려운듯
MAX_INT = 1000
MOD = 1000000007
n = int(input())
dp = [0] * (MAX_INT + 1)

dp[0] = 1
dp[1] = 2

for i in range(2, n+1):
    dp[i] = (2 * dp[i-1] + 3 * dp[i-2]) % MOD
    for j in range(i-3, -1, -1):
        dp[i] = (dp[i] + dp[j] * 2) % MOD


print(dp[n])
