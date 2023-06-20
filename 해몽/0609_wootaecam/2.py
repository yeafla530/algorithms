import sys

si = sys.stdin.readline
n, m, k = map(int, si().split())
diag = [[False for i in range(m+1)] for _ in range(n+1)]
MOD = 1000000007
for _ in range(k):
    r, c = map(int, si().split())
    diag[r-1][c-1] = True

dy = [[0 for _ in range(m+1)] for _ in range(n+1)] # dy[r][c] := r행 c열인 직사각형을 최단거리로 이동하는 경우의 수
dy[n][0] = 1

# 각 대각선을 사용하지 않는 경우
for r in range(n, -1, -1):
    for c in range(0, m+1):
        print(r, c)
        if r == n and c == 0:
            continue
        
        if c == 0 or r == n:
            dy[r][c] = 1

        else:
            dy[r][c] = (dy[r + 1][c] + dy[r][c-1]) % MOD

print(dy)
ans = 0
for r in range(n):
    for c in range(m):
        if not diag[r][c]:
            break
            
        # 대각선을 찾으면
        # 내가 최단거리로 이동하는 경우의 수를 누적해줌 
        
        # 대각선을 오른쪽 아래로 이동하는 경우
        ans += (dy[n-r-1][c] * dy[r+1][m-c-1]) % MOD

        # 대각선을 왼쪽 위로 이동하는 경우
        ans += (dy[n-r-1][c+1] * dy[r][m-c]) % MOD

print(ans)

'''
2 2 2
1 2
2 1
=> 12가 나와야하는데 6이 나온다 ㅠ
'''