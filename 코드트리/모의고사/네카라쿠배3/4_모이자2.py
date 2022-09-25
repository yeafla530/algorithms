import sys
INT_MAX = sys.maxsize

# 이동거리의 합이 최소
n = int(input())
arr = list(map(int, input().split()))
left = [0] * n
right = [0] * n

left[0] = 0
# 왼쪽에 있는 사람들의 합
left_prefix = arr[0]
for i in range(1, n):
    # i번째 왼쪽에 사는 사람들이 전부i번으로 모이기 위한 이동거리의 총 합
    # 이전까지 이동했던 거리의 합 + 다음으로 이동했을 때 거리를 계속 더해줌 
    left[i] = left[i-1] + left_prefix
    left_prefix += arr[i]
    # print(left_prefix)

right[n-1] = 0
right_prefix = arr[n-1]
for i in range(n-2, -1, -1):
    right[i] = right[i+1] + right_prefix
    right_prefix += arr[i]

# print(left, right)
result = INT_MAX
for i in range(n):
    s = left[i] + right[i]
    result = min(result, s)

print(result)
