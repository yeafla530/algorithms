import sys
si = sys.stdin.readline
N, X = map(int, si().split())
a = list(map(int, si().split()))

ans = sys.maxsize # 초기값

# select a number
for i in range(N):
    sum = a[i]
    if sum >= X:
        ans = min(ans, sum)

# select two number
for i in range(N-1):
    for j in range(i+1, N):
        sum = a[i] + a[j]
        if sum >= X:
            ans = min(ans, sum)


for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum = a[i] + a[j] + a[k]

            if sum >= X:
                ans = min(ans, sum)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)
