import sys
INT_MIN = -sys.maxsize
# 빨간색N개, 파란색N개, 뽑힌 카드들의 최대합
n = int(input())
red = [0] * (2*n+1)
blue = [0] * (2*n+1)
for i in range(1, 2*n+1):
    r, b = map(int, input().split())
    red[i] = r
    blue[i] = b

# 빨간색 n개, 파란색n개
# 최대합 

# 지금까지 뽑은 빨간색 카드 수, 현재 위치
# 지금까지 뽑은 파란색 카드 수, 현재 위치
# 모든 카드의 개수, 총합

# dp[i][j] :
# i번째 카드 쌍까지 고려해봤을 때
# 지금까지 빨간색 카드를 정확히 j장 뽑았다 했을 때
# 얻을 수 있는 뽑힌 숫자들의 최대 합

dp = [[INT_MIN]*(2*n+1) for _ in range(2*n+1)]

# 초기화
dp[0][0] = 0


for i in range(1, 2*n+1):
    # 빨간색 카드의 수
    for j in range(i+1):
        # Case1 : 현재 빨간색을 고르는 경우 (빨간카드를 골랐는데 0개일 수 없음)
        if j > 0:
            # 빨간카드가 하나 적은 경우이므로 j-1
            dp[i][j] = max(dp[i][j], dp[i-1][j-1]+red[i])
        # Case2 : 현재 파란색 카드를 고르는 경우 (파란색카드 골랐는데 0개일수 없음)
        if i - j > 0:
            # 빨간카드에 변화가 없어 j
            dp[i][j] = max(dp[i][j], dp[i-1][j]+blue[i])

print(dp[2*n][n])