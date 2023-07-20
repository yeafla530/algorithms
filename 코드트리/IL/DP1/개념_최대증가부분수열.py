n = int(input())
a = [0] + list(map(int, input().split()))

dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j]+1)


print(max(dp))


## LIS (0721)
# 가장 긴 부분 수열 의 길이
# 원소들이 계속 증가한다면 이 수열을 증가 부분수열이라 한다
# 최장 증가 부분수열 구하기
import sys
INT_MIN = -sys.maxsize

n = int(input())
arr = [0] + list(map(int, input().split()))

# 상태 : 선택한 수열의 위치, 부분수열의 길이가 길수록 좋음
# dp[i] : 현재 i위치까지의 부분수열길이 dp[i]
dp = [INT_MIN] * (n+1) 
dp[0] = 0

# dp[i]값은 i번째보다 앞에 있는 원소들 중 a[i]보다는 값이 작은 곳을 골라
# 그 뒤에 새로운 원소 a[i]를 추가해 최대 부분수열 길이 계산
# a[i]는 현재 위치, a[j]는 현재위치보다 이전의 값들
for i in range(1, n+1):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

