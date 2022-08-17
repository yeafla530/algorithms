MAX_NUM = 100
n, k = tuple(map(int, input().split()))
arr = [0] * (MAX_NUM + 1)
for _ in range(n):
    # 같은 바구니 위치가 나올 수 있음
    m, idx = map(int, input().split())
    arr[idx] += m
# print(arr)

max_sum = 0
# 중간값 = 4, k = 3 이면 1~7사이 수
for i in range(MAX_NUM):
    sum_all = 0
    for j in range(i - k, i + k + 1):
        if j >= 0 and j <= MAX_NUM: 
            sum_all += arr[j]
    max_sum = max(max_sum, sum_all)

print(max_sum)
