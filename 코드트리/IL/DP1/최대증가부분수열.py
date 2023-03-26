# LIS 문제 : 부분수열 
# dp[i] = 마지막으로 고른 원소의 위치가 i인 부분 수열 중 최장 부분 수열의 길이
# dp[i] = max(dp[j]) + 1

n = int(input())
arr = [0] + list(map(int, input().split()))

# 각자가 부분수열이기 때문에 1로 초기화
dp = [1 for _ in range(n+1)]
# dp[0]만들어주는 테크닉
dp[0] = 0


for i in range(1, n+1):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))