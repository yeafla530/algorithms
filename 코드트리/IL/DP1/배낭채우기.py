# 무게합이 m 넘지 않고 가치합은 최대가 되도록
import sys
INT_MIN = -sys.maxsize
# dp[w] = w무게일 때 최대 가치 / 무게가 동일할 경우 가치가 높을 수록 좋음
n, m = map(int, input().split())
bags = [list(map(int, input().split())) for _ in range(n)]
dp = [INT_MIN] * (m+1)
dp[0] = 0

for w, v in bags:
    for i in range(m, -1, -1):
        if i >= w:
            if dp[i-w] == INT_MIN:
                continue
            
            dp[i] = max(dp[i], dp[i-w] + v)

print(max(dp)) 