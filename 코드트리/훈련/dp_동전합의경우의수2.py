import sys

INT_NUM = 10000
INT_MAX = sys.maxsize

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
# O(nlogn)이 필요
ans = INT_MAX

# 1, 2, 3

dp = [INT_MAX] * (INT_NUM+1)
dp[0] = 0
for now_coin in range(1, k+1):
    for coin in coins:
        if now_coin >= coin:
            dp[now_coin] = min(dp[now_coin], dp[now_coin-coin] + 1)

if dp[k] == INT_MAX:
    print(-1)
else:
    print(dp[k])