# 겹치지 않게 하면서 얻을 수 있는 돈이 최대

# 최대 얻을 수 있는 돈
n = int(input())
# (s, e, p) : 시작 날짜, 끝나는 날짜, 금액
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * n
arr.sort()


for i in range(n):
    dp[i] = arr[i][2]
    for j in range(i):
        s_i, e_i, m_i = arr[i]
        s_j, e_j, m_j = arr[j]

        if s_i > e_j:
            money = dp[j] + m_i
            dp[i] = max(dp[i], money)

# print(dp)
print(max(dp))