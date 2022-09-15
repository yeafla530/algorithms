
import sys
MAX_INT = sys.maxsize

SIZE = 11000
n, m = map(int, input().split())
coins = list(map(int, input().split()))
coins.sort()
dp = [MAX_INT] * (SIZE*2 + 1)

for coin in coins:
    dp[SIZE+coin] = 1

# dp[i] = 거슬러 줄 수 있는 동전의 최소 개수
for i in range(SIZE+1, SIZE+m+1):
    for coin in coins:
        # print(20000-coin)
        dp[i] = min(dp[i-coin]+1, dp[i])

# print(dp[1:m+1])
if dp[SIZE+m] == MAX_INT:
    print(-1)
else:
    print(dp[SIZE+m])





