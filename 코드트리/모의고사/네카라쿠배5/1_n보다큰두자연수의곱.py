import sys

INT = 1000
n, x = map(int, input().split())
ans = sys.maxsize
for i in range(1, INT+1):
    for j in range(i, i+x+1):
        if i * j > n:
            ans = min(ans, i * j)

print(ans)

### 완탐 최적화
from math import sqrt
import sys

INT_MAX = sys.maxsize
n, x = map(int, input().split())
ans = INT_MAX

sq = int(sqrt(n))
# n의 제곱근 + 1 까지
for a in range(1, sq+2):
    # a * b > n => b > n // a => b의 최소: n//a+1
    b = max(a, n // a + 1)
    if b - a <= x:
        ans = min(ans, a * b)



print(ans)

