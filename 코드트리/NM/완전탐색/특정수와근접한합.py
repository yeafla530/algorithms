import sys

n, s = map(int, input().split())
arr = list(map(int, input().split()))
sum_num = sum(arr)
ans = sys.maxsize

for i in range(n-1):
    for j in range(i+1, n):
        # print(i, j)
        num = sum_num - arr[i] - arr[j]

        ans = min(ans, abs(num-s))        




print(ans)