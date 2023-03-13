n = int(input())
arr = [int(input()) for _ in range(n)]

standard = sum(arr) // n
# print(standard)

cnt = 0
for block in arr:
    if block > standard:
        cnt += block - standard

print(cnt)