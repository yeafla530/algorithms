import sys

INT = 1000
n, x = map(int, input().split())
ans = sys.maxsize
for i in range(1, INT+1):
    for j in range(i, i+x+1):
        if i * j > n:
            ans = min(ans, i * j)

print(ans)

