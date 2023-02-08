n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    arr[i][0] = 1
    arr[i][i] = 1
    for j in range(1, i):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

for i in range(n):
    for j in range(i+1):
        print(arr[i][j], end=" ")
    print()
