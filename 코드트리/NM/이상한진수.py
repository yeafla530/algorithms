import sys
arr = list(map(int, list(input())))
length = len(arr)
MiN_INT = -sys.maxsize

ans = MiN_INT

for i in range(length):
    arr[i] = 1 if arr[i] == 0 else 0

    s = 0
    for j in range(length):
        s = 2 * s + arr[j]
    
    arr[i] = 1 if arr[i] == 0 else 0
    if ans < s:
        ans = s

print(ans)