# 돌 n개
# 상근, 창영이는 턴을 번갈아가면서 돌을 가져감
# 1개 또는 3개 가져갈 수 있음
# 마지막 돌을 가져가는 사람이 이김

# 상근이가 먼저 시작

# n = int(input())

# ans = n
# moc = ans // 3
# ans %= 3

# if (moc + ans) % 2 == 0:
#     print("CY")
# else:
#     print("SK")


n = int(input())
dp = [-1] * 10001

dp[1] = 0 # SK
dp[2] = 1 # CY
dp[3] = 0

for i in range(4, n+1):
    if dp[i-1] == 0 or dp[i-3] == 0:
        dp[i] = 1
    else:
        dp[i] = 0

# print(dp)
if dp[n]:
    print("CY")
else:
    print("SK")