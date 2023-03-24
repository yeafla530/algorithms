n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (1001)


arr.sort()

for i in range(n):
    dp[i] = 1

    for j in range(i):
        x1_i, _ = arr[i]
        _, x2_j = arr[j]

        if x2_j < x1_i:
            dp[i] = max(dp[i], dp[j]+1)

ans = max(dp)
print(ans)