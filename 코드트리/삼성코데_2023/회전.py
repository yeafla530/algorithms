# 시계방향 3회전 = 반시계 방향 1회전
# 반시계방향 3회전 = 시계 방향 1회전
# 둘 중 하나의 함수만 짜면 된다
# for 문으로 돌리는거면 시계방향

n, m = 4, 6
arr = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24]]
temp = [[0]*n for _ in range(m)]

# 반복문

for i in range(m):
    for j in range(n):
        temp[i][j] = arr[n-1-j][i]


# zip함수
arr = list(map(list, zip(*arr[::-1])))


print(*temp, sep="\n")
print(*arr, sep="\n")


# 부분회전 
def next_rotate(i1, j1, i2, j2, cnt):
    len = i2-i1
    temp = [[0]*n for _ in range(n)]

    # 부분만 temp에 copy
    for i in range(i1, i2):
        for j in range(j1, j2):
            temp[i][j] = board[i][j]
        
    
    # 시계방향 회전
    for _ in range(cnt):
        temp = list(map(list, zip(*temp[::-1])))
    
    # 초기 point
    x = i1
    y = j1

    for i in range(n):
        for j in range(n):
            if temp[i][j]:
                copy_board[x][y] = temp[i][j]
                y += 1

                if y == j2:
                    y = j1
                    x += 1