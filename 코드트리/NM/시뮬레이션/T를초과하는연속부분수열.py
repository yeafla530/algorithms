n, t = map(int, input().split())
arr = list(map(int, input().split()))

ans, cnt = 0, 0
for i in range(n):
    if i != 0 and arr[i-1] > t and arr[i] > t:
        cnt += 1
    
    else:
        cnt = 1
    
    ans = max(ans, cnt)

print(ans)