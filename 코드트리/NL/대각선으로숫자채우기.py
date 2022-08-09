n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
# print(arr)

num = 2
arr[0][0] = 1
for i in range(1, m):
    # 마지막 열일경우 끝날때까지 반복
    y = i
    x = 0

    while y != -1 and x < n:
        arr[x][y] = num
        # print(x, y)
        num += 1
        y -= 1
        x += 1

for i in range(1, n):
    x = i 
    y = m-1
    while 0 <= x < n and 0 <= y < m:
        arr[x][y] = num
        # print(x, y)
        num += 1
        y -= 1
        x += 1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()