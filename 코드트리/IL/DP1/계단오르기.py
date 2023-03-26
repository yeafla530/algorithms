# MAX_N = 1000
# MOD = 10007

# n = int(input())
# dp = [0] * (MAX_N + 1)

# dp[0] = 1
# dp[1] = 0
# dp[2] = 1
# dp[3] = 1

# for i in range(4, n+1):
#     dp[i] = (dp[i-2] + dp[i-3]) % MOD

# print(dp[n])


MAX_N = 1000
MOD = 10007

n = int(input())
dp = [0] * (MAX_N + 1)

dp[0] = 1

# 이미 dp[i]가 무엇인지 알때
# 2칸을 점프하거나(dp[i+2]) 3칸을 점프(dp[i+3])하거나 둘중하나

# 과거에서 구했던 것을 이용해서 dp[i][j]를 채우거나
# 현재 dp[i][j]를 아니까 dp[i+2][j], dp[i+3][j]를 채우거나!
for i in range(0, n+1):
    dp[i+2] = (dp[i+2] + dp[i]) % MOD
    dp[i+3] = (dp[i+3] + dp[i]) % MOD

    # dp[i] = (dp[i-2] + dp[i-3]) % MOD

print(dp[n])