# Lower Bound

## Lower Bound란?

- 원하는 값 target 이상의 값이 최초로 나오는 위치
- 즉, target보다 같거나 큰 원소들 중 가장 작은 값
- 파이썬에서는 bisect_left로 많이 알려져있다
- 작은 값을 구하기 위해 min_idx라는 변수 활용해 초기값으로 답이 될 수 없는 최댓값인 n을 넣고 문제 해결

## 코드

```python
def lower_bound(target):
    left = 0
    right = n-1
    min_idx = n

    while left <= right:
        mid = (right + left) // 2

        # arr[mid]가 target보다 같거나 큰 경우 가능한 mid값들 중 최솟값이 되어야한다
        if arr[mid] >= target:
            min_idx = mid
            right = mid - 1
        else:
            left = mid + 1

    return min_idx


```
