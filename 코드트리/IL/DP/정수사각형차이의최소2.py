# 최솟값을 1부터 100까지 일일이 가정
# 최솟값 이상의 수들만 써서 이동한다는 가정하에
# 경로상에 놓여있는 수들 중 최댓값을 최소화하는 문제

# 모든 lower_bound를 잡아보며 그때마다 upper_bound값을 구해 
# upper_bound - lower_bound값 중 최솟값을 갱신해주면 원하는 답 얻을 수 있음

# 답인데 너무 어렵다

import sys

INT_MAX = sys.maxsize
MAX_R = 100

n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]

dp = [[INT_MAX]*n for _ in range(n)]

ans = INT_MAX


def initialize():

    dp[0][0] = num[0][0]

    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], num[i][0])
    
    for j in range(1, n):
        dp[0][j] = max(dp[0][j-1], num[0][j])


def solve(lower_bound):
    # lower_bond미만의 값은 사용할 수 없도록 num값 변경
    for i in range(n):
        for j in range(n):
            if num[i][j] < lower_bound:
                num[i][j] = INT_MAX

    # DP 초기값 설정
    initialize()

    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(min(dp[i-1][j], dp[i][j-1]), num[i][j])
    
    return dp[n-1][n-1]

# 최솟값을 k라 했을 때 lower_bound이상의 수들만 사용해 이동한다는 조건하에
# 최댓값을 최소로 만드는 dp문제 풀어줌

for lower_bound in range(1, MAX_R+1):
    upper_bound = solve(lower_bound)

    # 다 진행했음에도 INT_MAX라면
    # 이동이 불가하단 뜻이므로 패스
    if upper_bound == INT_MAX:
        continue
    
    ans = min(ans, upper_bound - lower_bound)


print(ans)