n, m = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(m):
    s = 0
    a, b = map(int, input().split())

    s = sum(arr[a-1:b])

    print(s)