import sys
INT_MIN = -sys.maxsize

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [INT_MIN] * (m+1)
dp[0] = 0

for i in range(1, m+1):
    for w, v in arr:
        if i >= w:
            if dp[i-w] == INT_MIN:
                continue
            
            dp[i] = max(dp[i], dp[i-w]+v)

print(max(dp))
