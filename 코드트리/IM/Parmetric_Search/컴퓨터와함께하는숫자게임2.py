import sys

m = int(input())
a, b = map(int, input().split())

def binary_search(start, end, target):
    left = start
    right = end
    count = 0
    while left <= right:
        mid = (right + left) // 2
        count += 1
        if mid == target:
            return count
        
        if mid > target:
            right = mid - 1
        else:
            left = mid + 1

    return count

min_num = sys.maxsize
max_num = -sys.maxsize
# 최대 10^5
for target in range(a, b+1):
    num = binary_search(1, m, target)
    min_num = min(min_num, num)
    max_num = max(max_num, num)

print(min_num, max_num)