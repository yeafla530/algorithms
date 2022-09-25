import sys
INT_MAX = sys.maxsize

n = int(input())
arr = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]
left = [0] * (n+1)
right = [0] * (n+1)

left[1] = 0
for i in range(2, n+1):
    left[i] = abs(arr[i][0] - arr[i-1][0]) + abs(arr[i][1]-arr[i-1][1]) + left[i-1]

right[n] = 0
for i in range(n-1, 0, -1):
    right[i] = abs(arr[i][0] - arr[i+1][0]) + abs(arr[i][1] - arr[i+1][1]) + right[i+1]


min_result = INT_MAX
for i in range(2, n-1):
    result = left[i-1] + right[i+1] + abs(arr[i+1][0] - arr[i-1][0]) + abs(arr[i+1][1] - arr[i-1][1])

    min_result = min(result, min_result)

print(min_result)