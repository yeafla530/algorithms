n = int(input())
a = [987654321] + list(map(int, input().split()))
dp = [0] * (n+1)

for i in range(n+1):
    for j in range(i):
        if a[i] < a[j]:
            dp[i] = max(dp[i], dp[j]+1)


print(max(dp))