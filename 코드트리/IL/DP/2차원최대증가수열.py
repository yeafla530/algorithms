# 점프 => 점프한 수가 더 커야함
# 한칸이상 대각선으로만 점프 가능
import sys
INT_MIN = -sys.maxsize

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[INT_MIN]*m for _ in range(n)]

dp[0][0] = 1
ans = 0
for i in range(1, n):
    for j in range(1, m):
        for k in range(i):
            for l in range(j):
                if dp[k][l] == INT_MIN:
                    continue
                if arr[i][j] > arr[k][l]:
                    dp[i][j] = max(dp[i][j], dp[k][l]+1)
                    ans = max(ans, dp[i][j])
# print(*dp, sep='\n')
print(ans)
