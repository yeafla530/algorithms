n = int(input())
arr = list(map(int, input().split()))

empty = []
max_idx = len(arr)

while True:
    result = 0
    for i in range(max_idx):
        if arr[i] > result:
            max_idx = i
            result = arr[i]

    
    empty.append(max_idx+1)
    if max_idx == 0:
        break 

print(*empty)