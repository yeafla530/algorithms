# 지금까지 선택한 동전의 합
# 지금까지 선택한 동전의 수

# 동전의 합이 같다면 사용한 동전의 개수가 많을수록 더 좋다
# dp[i] : 합 i를 만들기 위해 마지막으로 사용한 동전이 j번째 동전(coin[j])인경우
# dp[i] = dp[i-coin[j]] + 1

SIZE = 10001
n, m = map(int, input().split())
coins = [0] + list(map(int, input().split()))
# 최솟값을 찾는문제이므로 최대값으로 초기화
dp = [SIZE] * (m+1)

# 초기화
dp[0] = 0


# 가격
for i in range(1, m+1):
    # 0원 제외하고 
    for j in range(1, n+1):
        if i >= coins[j]:
            dp[i] = min(dp[i], dp[i-coins[j]] + 1)

min_cnt = dp[m]

if min_cnt == SIZE:
    min_cnt = -1

print(min_cnt)


