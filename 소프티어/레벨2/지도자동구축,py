n = int(input())
dp = [0] * 16
dp[0] = 2


for i in range(1, n+1):
    dp[i] = dp[i-1] + (dp[i-1]-1)


# print(dp)

print(dp[n]**2)