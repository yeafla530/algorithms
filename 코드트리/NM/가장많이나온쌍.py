n, m = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(m)]

def sum_tuple(i, j):
    cnt = 0
    for x, y in arr:
        if (i, j) in [(x, y), (y, x)]:
            cnt += 1
    
    return cnt


ans = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        ans = max(ans, sum_tuple(i, j))

print(ans)