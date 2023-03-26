n = int(input())
arr = [0] + list(map(int, input().split()))

# 최대 수익
dp = [0] * (n+1)

for i in range(1, n+1):
    for num in range(1, n+1):
        if i >= num:
            dp[i] = max(dp[i], dp[i-num]+arr[num])
            # print(i, num, i-num, dp)
print(dp[n])
        