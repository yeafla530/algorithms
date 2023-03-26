# 1) dp[i] : 선택한 연속 부분 수열의 마지막 원소의 위치가 i라 했을 때 얻을 수 있는 최대 점수 
# 2) dp[i] max(dp[i-1] + a[i], 2*a[i])
# 3) dp[0] = 2 * a[0]
import sys
INT_MIN = -sys.maxsize


n = int(input())
a = list(map(int, input().split()))

min_val = INT_MIN

dp = [
    INT_MIN
    for _ in range(n+5)
]

# 초기값
dp[0] = a[0]

for i in range(1, n):
    dp[i] = max(dp[i-1] + a[i], a[i])

print(max(dp))