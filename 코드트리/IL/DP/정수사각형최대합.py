# 1) dp[i]가 무엇인지정의
# 2) 점화식
# 3) 초기조건, 종료조검 

# 1) dp[i][j] = 마지막으로 방문했을 때(i,j) 얻을 수 있는 최대합
# 2) dp[i-1][j] dp[i-1][j-1] 중 최대값 => max(dp[i-1][j], dp[i-1][j-1])
# 3) 초기조건 : dp[0][0], 종료조건 i == n-1

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 메모이제이션
memo = [
    [-1] * n 
    for _ in range(n)
]

dxs = [0, 1]
dys = [1, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# x, y로부터 n-1, n-1 까지 최대 거리를 리턴하는함수
def find_max_sum(x, y):
    # 이미 계산됨
    if memo[x][y] != -1:
        return memo[x][y]
    # 종료 조건
    if x == n-1 and y == n-1:
        return graph[n-1][n-1]
    
    # 점화식
    # memo[x][y] = -1
    max_sum = 0
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if in_range(nx, ny):
            max_sum = max(memo[x][y], find_max_sum(nx, ny)+ graph[x][y])
    memo[x][y] = max_sum
    return memo[x][y]

find_max_sum(0, 0)
print(memo[n-1][n-1])




# dp = [[0]*n for _ in range(n)]

# def initial():
#     dp[0][0] = graph[0][0]
#     # 오른쪽으로만 이동
#     for i in range(1, n):
#         dp[0][i] = dp[0][i-1] + graph[0][i]
    
#     for i in range(1, n):
#         dp[i][0] = dp[i-1][0] + graph[i][0]

# initial()


# for i in range(1, n):
#     for j in range(1, n):
#         dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + graph[i][j]
    
# print(dp[n-1][n-1])