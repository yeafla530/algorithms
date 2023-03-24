MAX_K = 2

n = int(input())
arr = list(map(int, input().split()))

# dp[i][j] : 마지막으로 고른 원소의 위치가 i이면서 현재 증가-감소 상태가 j일때
# 증가중이면 j = 0, 감소 j = 1
dp = [[0]*MAX_K for _ in range(n)]

for i in range(n):
    dp[i][0] = 1
    dp[i][1] = 1

    for j in range(i):
        # 증가하는 경우에는
        if arr[j] < arr[i]:
            dp[i][0] = max(dp[i][0], dp[j][0] + 1)

        
        # 감소하는 경우에는
        if arr[j] > arr[i]:
            dp[i][1] = max(dp[i][1], dp[j][1] + 1)

    
    dp[i][1] = max(dp[i][1], dp[i][0])


ans = 0
for i in range(n):
    for j in range(MAX_K):
        ans = max(ans, dp[i][j])

print(ans)