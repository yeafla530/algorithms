n, m = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(m):
    target = int(input())
    find = False
    left = 0
    right = n-1

    while right >= left:
        mid = (left+right)//2

        if arr[mid] == target:
            print(mid+1)
            find = True
            break 
        
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    if find == False:
        print(-1)
    