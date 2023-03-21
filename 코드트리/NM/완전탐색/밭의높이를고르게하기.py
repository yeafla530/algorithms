n, h, t = map(int, input().split())
arr = list(map(int, input().split()))

# 연속하게 최소 T번이상 H높이로 나오게끔
for i in range(len(arr)):
    arr[i] = abs(arr[i]-h)

min_result = 987654321

for i in range(n-t+1):
    count = 0

    for j in range(t):
        count += arr[i+j]

    min_result = min(min_result, count)

print(min_result)