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


# 시간초과 정답
# 변수 선언 및 입력:
n = int(input())
arr = list(map(int, input().split()))
possible_sums = set()


def combination(idx, sum_val):
    # 종료조건이 되면
    # 퇴각합니다.
    if idx == n:
        # 가능한 합으로 기록합니다.
        possible_sums.add(sum_val)
        return

    # idx번지 수를 선택하지 않는 경우입니다.
    combination(idx + 1, sum_val)
    # idx번지 수를 선택하는 경우입니다.
    combination(idx + 1, sum_val + arr[idx])

   
# 만들어낼 수 있는 모든 합을 찾아봅니다.
combination(0, 0)

# 1부터 순서대로 보며
# 불가능한 최초의 수를 출력합니다.
num = 1
while True:
    # 찾을 수 없다면
    # 답을 출력합니다.
    if num not in possible_sums:
        print(num)
        break

    # 그 다음 수로 넘겨줍니다.
    num += 1