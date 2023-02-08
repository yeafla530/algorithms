import sys

n = int(input())
arr = list(map(int, input().split()))


result = sys.maxsize
for i in range(n-1, -1, -1):
    for j in range(i-1, -1, -1):
        if arr[i] - arr[j] < result:
            result = arr[i] - arr[j]

print(result) 