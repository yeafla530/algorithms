# 특정한 위치에 있는 병사를 열외시키는 방법 이용
# 남아있는 병사 수가 최대가 되도록
# 내림차순 형태가 되어야함

# 가장 긴 "증가하는" 부분수열(LIS) 알고리즘 응용
# 모든 0 < j < i에 대하여, D[i] = max(D[i], D[j]+1) if array[j] < array[i]

n = int(input())
array = list(map(int, input().split()))
array.reverse()
dp = [1] * (n+1)

for i in range(1, n):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-dp[n-1])
