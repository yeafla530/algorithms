n = int(input())

# 더 적은 개수의 봉지
dp = [5001] * (n+1)
suger = [3, 5]
dp[0] = 0

for i in range(len(suger)):
    for j in range(suger[i], n+1):
        dp[j] = min(dp[j-suger[i]]+1, dp[j])
# print(dp)
if dp[n] == 5001:
    print(-1)
else:
    print(dp[n])