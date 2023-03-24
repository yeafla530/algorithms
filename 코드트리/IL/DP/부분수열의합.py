n, m = map(int, input().split())
arr = list(map(int, input().split()))

dp = [0] * (m+1)
dp[0] = 1
for num in arr:
    for i in range(m, -1, -1):
        if i >= num:
            if dp[i-num] == 0:
                continue
            
            dp[i] = dp[i-num] + 1
        # print(num, dp)

if dp[m] != 0:
    print('Yes')
else:
    print('No')