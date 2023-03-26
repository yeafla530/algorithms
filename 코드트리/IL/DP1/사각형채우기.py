# 메모이제이션 - 탑다운
yMOD = 10007
MAX_INT = 1000

n = int(input())
memo = [0] * (MAX_INT+1)

memo[0] = 1
memo[1] = 1

for i in range(2, n+1):
    memo[i] = (memo[i-1] + memo[i-2]) % MOD

# print(memo)
print(memo[n])

# dp (바텀업 - 동적계획법)
MOD = 10007
MAX_INT = 1000

n = int(input())

dp = [0] * (MAX_INT + 1)
dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % MOD

print(dp[n])