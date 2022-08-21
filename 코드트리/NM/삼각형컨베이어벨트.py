n, t = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

arr = a + b + c

for i in range(t):
    arr = arr[-1:] + arr[:-1]
# print(arr)
for i in range(3):
    # print(i*n, (i+1)*n)
    print(*arr[i*n:(i+1)*n])

