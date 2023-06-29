import sys
si = sys.stdin.readline

n = int(si())
a = [list(map(int, si().split())) for _ in range(n)]


# 좌우반전
def lr_flip(a):
    b = [[0 for _ in range(n)] for _ in range(n)] # 뒤집은 결과를 저장하는 배열

    for i in range(n):
        for j in range(n):
            # 원래 좌표가 (i, j) => 좌우반전 (i, n-1-j)
            b[i][n-1-j] = a[i][j]
    
    return b

# 상하반전
def ud_flip(a):
    b = [[0 for _ in range(n)] for _ in range(n)] # 뒤집은 결과를 저장하는 배열

    for i in range(n):
        for j in range(n):
            # 원래 좌표가 (i, j) => 상하반전 (n-1-i, j)
            b[n-1-i][j] = a[i][j]
    
    return b



a1 = a
a2 = lr_flip(a)
a3 = ud_flip(a)
a4 = lr_flip(a3)

for i in range(n):
    print(*(a1[i] + a2[i]))

for i in range(n):
    print(*(a3[i] + a4[i]))

'''
3
1 2 3 
4 5 6 
7 8 9
'''