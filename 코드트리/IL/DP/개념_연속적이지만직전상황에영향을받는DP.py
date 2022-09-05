import sys
INT_MIN = -sys.maxsize

n = 4
dp = [
    [0]*4
    for _ in range(n+1)
]

a = [
    [0, 0, 0, 0],
    [0, 1, 2, 5],
    [0, 3, 4, 8],
    [0, 2, 7, 5],
    [0, 4, 2, 3]
]

def initial():
    for i in range(1, n+1):
        for j in range(1, 4):
            dp[i][j] = INT_MIN

    for j in range(1, 4):
        dp[1][j] = a[1][j]

initial()

# i = 몇번째까지 선택
for i in range(2, n+1):
    # j = 마지막으로 고른 숫자의 위치
    for j in range(1, 4):
        # k = 바로 직전에 고른 숫자의 위치
        for k in range(1, 4):
            if j != k:
                dp[i][j] = max(dp[i][j], dp[i-1][k]+a[i][j])


ans = 0
for j in range(1, 4):
    ans = max(ans, dp[n][j])

print(ans)