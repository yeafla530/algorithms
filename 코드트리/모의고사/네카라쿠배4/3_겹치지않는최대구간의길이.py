
n = int(input())
arr = list(map(int, input().split()))
result = 0

for i in range(n):
    h = set()

    for j in range(i, n):
        if arr[j] in h:
            break
        
        h.add(arr[j])

    result = max(result, len(h))



print(result)