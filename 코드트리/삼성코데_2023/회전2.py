n, m = 4, 6
arr = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24]]
temp = [[0]*n for _ in range(m)]

# 시계방향 회전
for i in range(m):
    for j in range(n):
        temp[i][j] = arr[n-1-j][i]


for i in range(m):
    for j in range(n):
        print(temp[i][j], end=" ")
    print() 

print()
temp = [[0]*n for _ in range(m)]

# 반시계 방향 회전
for i in range(m):
    for j in range(n):
        temp[m-1-i][j] = arr[j][i]

for i in range(m):
    for j in range(n):
        print(temp[i][j], end=" ")
    print() 

# 시계방향
arr = list(map(list, zip(*arr[::-1])))
# 반시계방향
arr2 = list(map(list, zip(*arr)))[::-1]
print(*arr, end=" ")
print()
print(*arr2, end=" ")

