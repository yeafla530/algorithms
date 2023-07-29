import sys
# O(n^2)안됨 
n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))

j = 0
ans = -sys.maxsize
s = 0
cnt = 0
if k == 1:
    print(max(arr))
else:
    for i in range(1, n-k+2):
        while j+1 <= n and cnt != k:
            cnt += 1
            j += 1
            s += arr[j]
        
        if cnt == k:
            cnt -= 1
            ans = max(ans, s)
            s -= arr[i]

    print(ans)