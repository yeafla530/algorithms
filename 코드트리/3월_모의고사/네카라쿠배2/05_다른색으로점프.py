MOD = 10007

# 변수 선언 및 입력: 
n, m = tuple(map(int, input().split()))
grid = [
    input().split()
    for _ in range(n)
]
dp = [
    [0] * m
    for _ in range(n)
]

dp[0][0] = 1
for i in range(n):
    for j in range(m):
        for k in range(i):
            for l in range(j):
                # (i, j)에 도달하기 바로 직전의 위치를
                # (k, l)이라 했을 때
                # 가능한 가지수를 갱신합니다.
                if grid[k][l] != grid[i][j]:
                    dp[i][j] = (dp[i][j] + dp[k][l]) % MOD

print(dp[n - 1][m - 1])