# 변수 선언 및 입력:
n = int(input())
arr = list(map(int, input().split()))
   
# Step 1: n개의 수를 오름차순으로 정렬합니다.
arr.sort()

# Step 2: 표현이 가능한 범위를 확장시키다
#         불가능한 상황이 오면 그때가 답이 됩니다.
sum_val = 0
for elem in arr:
    if sum_val + 1 < elem: 
        break
    sum_val += elem

# 출력:
print(sum_val + 1)