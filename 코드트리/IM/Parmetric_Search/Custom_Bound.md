# Custom Bound

## target보다 같거나 작은 숫자들 위치 중 가장 큰 위치

```python
arr = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9]
target = 4 # idx 8이 최대수

def custom_bound(target):
    left = 0
    right = n-1
    max_idx = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] <= target:
            max_idx = max(max_idx, mid)
            left = mid + 1
        else:
            right = mid - 1

    return -1

```
