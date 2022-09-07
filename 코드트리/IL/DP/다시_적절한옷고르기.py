import sys
INT_MIN = -sys.maxsize
# n = 옷수, m = 일수
n, m = map(int, input().split())
s = [0] * (n+1)
e = [0] * (n+1)
v = [0] * (n+1)

# dp[i][j] : i번째 날까지 입을 옷 전부 결정했고, 마지막 날에 입은 옷이 j옷이라고 했을 때, 얻을 수 있는 최대 만족도
dp = [[0]*(n+1) for _ in range(m+1)]

def initialize():
    for i in range(1, m+1):
        for j in range(1, n+1):
            dp[i][j] = INT_MIN

    for j in range(1, n+1):
        if s[j] == 1:
            dp[1][j] = 0


for i in range(1, n+1):
    s[i], e[i], v[i] = tuple(map(int, input().split()))

initialize()

for i in range(2, m+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            # i-1번째 날에 k번 옷을 입은 경우 고려
            # 단 k번 옷이 i-1번째 날에 입을 수 있어야하고 j번 옷이 i번째 날에 입을 수 있는 경우에만 고려
            # j번 옷이 i번째 날에 입을 수 있는 경우에만 고려해볼 수 있음
            if s[k] <= i-1 <= e[k] and s[j] <= i <= e[j]:
                dp[i][j] = max(dp[i][j], dp[i-1][k] + abs(v[j] - v[k]))


ans = max(dp[m][1:n+1])
print(ans)