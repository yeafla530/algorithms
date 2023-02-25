def solution(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        
        if arr[mid] > target:
            right = mid - 1 
        else:
            left = mid + 1 

    return -1

arr = [4, 8, 9, 12, 15, 18, 23, 24, 24, 26, 27, 29, 31]
target = 24
print(solution(arr, target))