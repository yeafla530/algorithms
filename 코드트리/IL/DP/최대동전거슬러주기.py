import sys
INT_MIN = -sys.maxsize

n, m = map(int, input().split())
coins = list(map(int, input().split()))

dp = [INT_MIN] * (m+1)
dp[0] = 0

for i in range(1, m+1):
    for coin in coins:

        if i >= coin:
            # print(i-coin, i, coin)
            if dp[i-coin] == INT_MIN:
                continue
            dp[i] = max(dp[i], dp[i-coin]+1)
            # print(dp)

# print(dp)
print(dp[m] if dp[m] != INT_MIN else -1)

