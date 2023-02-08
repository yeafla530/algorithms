# 최대 이익 출력
n = int(input())
arr = list(map(int, input().split()))

result = 0
for i in range(n):
    for j in range(i, n):
        if arr[j] - arr[i] > result:
            result = arr[j] - arr[i]

print(result)