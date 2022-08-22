n, m = map(int, input().split())
arr = []

# 해설 풀이
# 몇개 들어있는지
def combination(cnt, last_num):
    # 종료조건
    if cnt == m:
        print(*arr)
        return
    # 재귀함수
    for i in range(last_num+1, n+1):
        # 2를 봤으면 3~5중 골라라
        arr.append(i)
        combination(cnt+1, i)
        arr.pop()

combination(0, 0)

# 강사님 풀이
# curr_num을 포함할지 말지 (0 / 1)
# 포함하는 아이템의 번호는 curr_num
# cnt : 몇 개의 아이템(1)이 포함되었는지
# def combination(curr_num, cnt):
#     # 종료조건
#     if curr_num == n+1:
#         if cnt == m:
#             print(*arr)
#         return

#     # 오름차순으로 출력하기 위해 순서도 중요
#     # curr_num이 포함 되는 경우
#     arr.append(curr_num)
#     combination(curr_num+1, cnt+1)
#     arr.pop()

#     # curr_num이 포함 안되는 경우
#     combination(curr_num+1, cnt)

# combination(1, 0)



# 내 풀이
# def print_of_num():
#     for i in range(len(arr)):
#         if arr[i]:
#             print(i+1, end=" ")
#     print()

# def choose(cnt, num):
#     if cnt == n:
#         if sum(arr) == m:
#             print_of_num()
#         return

#     for i in range(2):
#         arr.append(i)
#         # print(arr)
#         choose(cnt+1, num+1)
#         arr.pop()

# choose(0, 1)