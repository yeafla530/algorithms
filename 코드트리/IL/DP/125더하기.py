MAX_M = 3
MOD = 10007

n = int(input())
numbers = [1, 2, 5]
dp = [0] * (n+1)

dp[0] = 1

for i in range(1, n+1):
    # 마지막으로 고른 숫자가 num인 경우에 대해 가지수 더해줌 
    for num in numbers:
        if i >= num:
            dp[i] = (dp[i]+dp[i-num]) % MOD
            # print(dp)

print(dp[n])


