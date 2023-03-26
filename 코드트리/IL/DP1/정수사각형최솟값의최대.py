# 


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dp = [[[] for _ in range(n)] for _ in range(n)]
# print(dp)

def initial():
    dp[0][0].append(a[0][0])

    for i in range(1, n):
        dp[0][i] = [*dp[0][i-1]]
        dp[0][i].append(a[0][i])
    for i in range(1, n):
        dp[i][0] = [*dp[i-1][0]]
        dp[i][0].append(a[i][0])

initial()

for i in range(1, n):
    for j in range(1, n):
        if min(dp[i-1][j]) >= min(dp[i][j-1]):
            dp[i][j] = [*dp[i-1][j]]
            dp[i][j].append(a[i][j])
        else:
            dp[i][j] = [*dp[i][j-1]]
            dp[i][j].append(a[i][j])




# print(*dp, sep="\n")
print(min(dp[n-1][n-1]))


# 정답풀이
# 시작점에서 출발해 마지막으로 방문한 위치
# 선택된 경로에서 최솟값
n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

def initial():
    dp[0][0] = num[0][0]
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][0], num[i][0])
    for j in range(1, n):
        dp[0][j] = min(dp[0][j-1], num[0][j])


initial()

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = min(max(dp[i-1][j], dp[i][j-1]), num[i][j])

print(dp[n-1][n-1])
