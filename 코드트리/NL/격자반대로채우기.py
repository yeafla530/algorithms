n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]

is_up = True
num = 1
for j in range(n-1, -1, -1):
    if is_up:
        for i in range(n-1, -1, -1):
            arr[i][j] = num
            # print(i, j)
            num += 1
        is_up = False
    else:
        for i in range(n):
            arr[i][j] = num
            num += 1
        is_up = True


for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()