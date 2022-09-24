import sys
MAX_INT = sys.maxsize

n, m = map(int, input().split())
coins = [0] + list(map(int, input().split()))

dp = [MAX_INT] * (m+1)
dp[0] = 0

for i in range(1, m+1):
    for j in range(1, n+1):
        if i >= coins[j]:
            dp[i] = min(dp[i], dp[i-coins[j]]+1)

min_cnt = dp[m]
if min_cnt == MAX_INT:
    min_cnt = -1
print(min_cnt)
