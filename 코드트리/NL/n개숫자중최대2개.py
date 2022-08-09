# N개의 정수를 내림차순으로 정렬
n = int(input())
arr = list(map(int, input().split()))

max1, max1_idx = arr[0], 0

for i in range(1, n):
    if arr[i] > max1:
        max1, max1_idx = arr[i], i
    
is_init = False
for i in range(n):
    if i == max1_idx:
        continue
    # 맨 처음 index인 경우 
    # max2 초기화
    if not is_init:
        is_init, max2 = True, arr[i]
    
    # 그 외 비교 
    elif arr[i] > max2:
        max2 = arr[i]

print(max1, max2)



# 두번째 풀이
# N개의 정수를 내림차순으로 정렬
n = int(input())
arr = list(map(int, input().split()))

if arr[0] > arr[1]:
    max1, max2 = arr[0], arr[1]

else:
    max2, max1 = arr[0], arr[1]


for i in range(2, n):
    # Case 1 : 지금까지 본 숫자들보다 좋다면
        #          max2, max1 모두 갱신해줍니다.
    if arr[i] >= max1:
        max2, max1 = max1, arr[i]
        
     # Case 2 : max2보다만 좋다면 max2를 갱신합니다.
    elif arr[i] > max2:
        max2 = arr[i]

print(max1, max2)