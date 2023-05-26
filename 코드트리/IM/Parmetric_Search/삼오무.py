import sys
INT_MAX = sys.maxsize

n = int(input())

def get_num_of_numbers(mid):
    moo_cnt = mid // 3 + mid // 5 - mid // 15

    return mid - moo_cnt

# 4번째 수
# 1~k사이 적혀있는 서로 다른 숫자 N이상인 경우 가능한 K의 최솟값 구하기
left = 1
right = INT_MAX
min_num = INT_MAX

while left <= right:
    mid = (left + right) // 2

    if get_num_of_numbers(mid) >= n:
        right = mid - 1
        min_num = min(min_num, mid)

    else:
        left = mid + 1

print(min_num)