n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
k -= 1
top = 0
for i in range(n-1, 0, -1):
    for j in range(k, k+m):
        if arr[i][j] == 1:
            top = i

# print(top)
for i in range(k, k+m):
    arr[top-1][i] = 1

for i in range(n):
    print(*arr[i][:])