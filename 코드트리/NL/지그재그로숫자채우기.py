n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
x = 0
num = 0
is_up = True
for i in range(m):
    # m 짝 홀인 경우 나눠 생각
    if i % 2 == 0:
        for j in range(n):
            arr[j][i] = num
            num += 1
        
    else:
        for j in range(n-1, -1, -1):
            arr[j][i] = num
            num += 1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()
