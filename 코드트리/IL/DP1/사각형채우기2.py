MAX_INT = 1001
n = int(input())

dp = [0] * (MAX_INT)

dp[1] = 1
dp[2] = 3

if n >= 3:
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + 2 * dp[i-2]) % 10007

print(dp[n])