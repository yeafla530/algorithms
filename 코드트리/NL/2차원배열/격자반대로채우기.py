n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]

num = 1
up = True
for j in range(n-1, -1, -1):
    if up:
        for i in range(n-1, -1, -1):
            arr[i][j] = num
            num += 1
        up = not(up)

    else:
        for i in range(n):
            arr[i][j] = num
            num += 1
        up = not(up)

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()