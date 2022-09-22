n = int(input())
arr = [int(input()) for _ in range(n)]

standard = sum(arr) // n

arr.sort(reverse=True)

cnt = 0
i = n-1
while arr[0] != standard:
    num = arr[0] - standard
    arr[0] = standard
    cnt += num

    arr.sort(reverse=True)

print(cnt)
    

### 간단 풀이 
n = int(input())
arr = [int(input()) for _ in range(n)]

standard = sum(arr) // n


cnt = 0
for block in arr:
    if block > standard:
        cnt += block - standard

print(cnt)
    