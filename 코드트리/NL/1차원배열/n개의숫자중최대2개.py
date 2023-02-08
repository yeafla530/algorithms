n = int(input())
arr = list(map(int, input().split()))

if arr[0] > arr[1]:
    first, second = arr[0], arr[1]
else:
    first, second = arr[1], arr[0] 

for i in range(2, n):
    if arr[i] >= first:
        second, first = first, arr[i]

    elif arr[i] >= second:
        second = arr[i]

print(first, second)
