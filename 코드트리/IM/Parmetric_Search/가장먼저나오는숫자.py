n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

def lower_bound(target):
    left = 0
    right = n-1
    min_idx = n
    find = False

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            if arr[mid] == target:
                find = True
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1
    

    return min_idx+1 if find else -1




for num in nums:
    print(lower_bound(num))