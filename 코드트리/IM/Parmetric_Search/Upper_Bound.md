# Upper Bound

## Upper Bound란?

- 원하는 값 target을 초과하는 값이 최초로 나오는 위치
- python 에서는 bisect_right라는 이름으로 더 알려져 있다

## Lower Bound코드

```python
def upper_bound(target):
    left = 0
    right = n-1
    min_idx = n

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            min_idx = min(min_idx, mid)
            right = mid - 1

        else:
            left = mid + 1

    return min_idx

```
