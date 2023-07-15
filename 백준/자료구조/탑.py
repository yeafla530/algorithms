# # 나의 풀이
# n = int(input())
# a = [0] + list(map(int, input().split()))
# store = []
# result = []

# result.append(0)
# store.append(1)
# # 송전탑 확인
# for i in range(2, n+1):
#     unblock = []
#     # 저장된 index값
#     for j in range(len(store)-1, -1, -1):
#         # 현재 송전탑보다 비교한 송전탑이 더 큰 경우
#         s = store[j]
#         if a[s] >= a[i]:
#             # 부딪히는 송전탑
#             result.append(s)
#             # 비교할 송전탑에 현재 index넣기
#             store.append(i)
#             break
#         # 부딪히지 않을 경우
#         else:
#             # 끝까지 확인했을 때
#             if j == 0:
#                 result.append(0)
#             # 부딪히지 않은 store[j] 송전탑
#             unblock.append(j)

#     # result에 들어간 index까지만 저장 
#     for u in unblock:
#         store.pop(u)
#     store.append(i)

# print(*result)

# 스택 => 시간초과 N^2
# n = int(input())
# arr = list(map(int, input().split()))
# answer = []

# # 왼쪽 확인
# for i in range(n):
#     stack = []
#     idx = i
#     stack.append(arr[i])
#     # i부터 시작해서 왼쪽으로 (-1)
#     while idx-1 >= 0:
#         idx -= 1
#         # 만약 왼쪽 값보다 현재 송전탑이 더 높을 경우
#         if stack[0] > arr[idx]: 
#             stack.append(arr[idx])
#         else:
#             answer.append(idx+1)
#             break

#     if idx == 0:
#         answer.append(0)
        
# print(*answer)




# O(N) 풀이
# 탑마다 자신의 왼쪽에 있는 모든 탑을 볼 필요 있나?
# => 비교할 가치가 있는 탑만 기억하자
# # 스택 사용 다른사람 풀이
n = int(input())
a = list(map(int, input().split()))
# (index, value) 담는다
stack = []
answer = [0] * n

# 현재 탑보다 길이가 작은 탑을 만나면 pop해준다
# 왜냐? 그 다음 탑들도 제거한 탑을 만나지 못하기 때문 
# 현재 탑 이후 작은 탑은 다른 그 이후의 탑들도 만나지 못함
 
for i, tower in enumerate(a):
    # 현재 탑보다 앞에 낮은 탑이 존재할 때
    # pop한 이후에도 현재탑보다 높은 탑이 나올 때까지 제거
    while stack and stack[-1][1] <= tower:
        # 비교대상에서 제거
        stack.pop()
    
    # stack이 있는 경우(제거되지 않은 경우)
    # 현재 탑보다 높음
    if stack:
        answer[i] = stack[-1][0]

    # 현재 탑보다 낮은 탑은 전부 제거되고
    # 현재 탑만이 PUSH된다
    stack.append((i+1, tower))
    print(stack[-1])


print(*answer)