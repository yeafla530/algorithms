import sys
n, m = map(int, input().split())
arr = list(map(int, input().split()))

max_s = -sys.maxsize
for i in range(n-m+1):
    s = 0
    for j in range(i, i+m):
        s += arr[j]

    max_s = max(max_s, s)

print(max_s) 