import sys
si = sys.stdin.readline

n, K = map(int, si().split()) # 용액 개수, 횟수

comb = [list(map(int, si().split())) for _ in range(n)] # 조합표

A = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        # A[i][j] := j번 용액이 누군가랑 석여서 i번 용액이 되는 경우의 수
        A[i][j] = comb[j].count(i)

print(A)
dp = [[0 for _ in range(n)] for _ in range(K+1)]

# 초기값 설정
for i in range(n):
    dp[1][i] = 1

print(dp)


MOD = 1000000007
for cnt in range(2, K+1):
    for i in range(n):
        for j in range(n):
            dp[cnt][i] += A[i][j] * dp[cnt-1][j]
            dp[cnt][i] %= MOD
            print(dp)

print(*dp[K])

'''
2 3
0 1
1 0 

=> 4 4

2 4
0 0
0 0

=> 16 0

3 10
0 1 2
1 2 1
2 1 0

=> 9842 9510 9676

'''