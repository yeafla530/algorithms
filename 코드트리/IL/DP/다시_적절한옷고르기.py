# n = 옷수, m = 일수
n, m = map(int, input().split())
a = [[0]*(m+1) for _ in range(n+1)]
dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    s, e, v = map(int, input().split())
    for j in range(s, e+1):
        a[i][j] = v
# print(a)
# initial
for i in range(1, n+1):
    dp[i][1] = 0


# print(a)

# 일수는 고정
for i in range(2, m+1):
    # j = i일수에 선택한 옷
    for j in range(1, n+1):
        # k = 그 전에 고른 옷의 번호
        for k in range(1, n+1):
            # # 지금 선택한 옷의 화려함, 그 전에 선택한 옷의 화려함
            if a[j][i] and a[k][i-1] and a[k][i]:
                # 화려함의 차이를 더한 최대값
                # print(i)
                dp[j][i] = max(dp[j][i], dp[k][i-1] + abs(a[k][i-1] - a[j][i]))
                print(j, i, k)
                print(dp[j][i])
                print(dp[k][i-1] + abs(a[k][i] - a[j][i]))
                print()
print(dp)
max_num = 0
for i in range(1, n+1):
    max_num = max(dp[i][m], max_num)

print(max_num)

            