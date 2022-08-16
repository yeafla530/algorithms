import sys

n = int(input())
arr = list(map(int, input().split()))

INT_MIN = -sys.maxsize
ans = INT_MIN
for i in range(n-2):
    for j in range(i+2, n):
        ans = max(ans, arr[i] + arr[j])
    
print(ans)
