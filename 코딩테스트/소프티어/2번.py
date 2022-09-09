import sys

si = sys.stdin.readline
N, B = map(int, si().split())
a = list(map(int, si().split()))

ans = 0
for j in range(n):
    left, right = 0
    for i in range(j):
        if a[i] < a[j]:
            left += 1
        
    for k in range(j+1, n):
        if a[j] > a[k]:
            right += 1
    
    ans += left + right

print(ans)