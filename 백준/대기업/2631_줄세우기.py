n = int(input())
arr = [0] + [int(input()) for _ in range(n)]

dp = [0] * (n+1)

for i in range(1, n+1):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)
        

print(n-max(dp))