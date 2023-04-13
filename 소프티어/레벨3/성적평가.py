# n = int(input())

# # 0 ~ 1000이하 정수 점수 얻는다
# # 한 대회에서 둘 이상ㅇ 참가자가 동점 나올 수 있다

# total_score = [[0, i] for i in range(n)] 
# for _ in range(3):
#     player = list(map(int, input().split()))
#     arr = []
#     for i in range(n):
#         score = player[i]
#         total_score[i][0] += score
#         arr.append((score, i))

#     # 정렬
#     arr.sort(key = lambda x : -x[0])
#     # print(arr)

#     cnt = 1
#     same = 0
#     rank = [0] * n

#     for i in range(n-1):
#         if arr[i][0] == arr[i+1][0]:
#             rank[arr[i][1]] = cnt - same
#             same += 1
        
#         elif arr[i][0] > arr[i+1][0]:
#             rank[arr[i][1]] = cnt - same
#             same = 0

#         cnt += 1
#     rank[arr[n-1][1]] = cnt - same

#     print(*rank)


# total_cnt = 1
# total_rank = [0] * n
# same = 0

# # print(total_score)
# for i in range(n-1):
#     if total_score[i][0] > total_score[i+1][0]:
#         total_rank[arr[i][1]] = total_cnt - same
#         same = 0
    
#     else:
#         total_rank[total_score[i][1]] = total_cnt - same
#         same += 1

#     total_cnt += 1

# # print(total_cnt - same)
# total_rank[total_score[n-1][1]] = total_cnt - same

# print(*total_rank)

# # 1. 등수 계싼
# 임시 저장하는 temp만들어 받아줌 직전 사람보다 점수가 낮으면 직전 사람 등수에 1더한 것이 다음 사람 등수
# 최대 20만명 참여할 수 있도록 시간복잡도 고려
# NlogN이면 해결 가능

# # 2. 최초 등수 계산
# 최종결과 저장하는 result만들어 입력된 값들 동시에 더해줌


n = int(input())
arr = [list(map(int, input().split())) for _ in range(3)]

total_score = [0] * n

for i in range(len(arr)):
    result = [] # 각 대회 우승 결과 저장

    # 최대 10만
    for a in range(n):
        rank = 1
        total_score[a] += arr[i][a] # 참가자 점수 누적 계산
        for b in range(n):
            if arr[i][a] < arr[i][b]: # 모든 요소와 비교해 작을때만 랭크 1더함
                rank += 1
        
        result.append(rank)
    
    print(*result)

total_rank = []
for a in range(n):
    rank = 1
    for b in range(n):
        if total_score[a] < total_score[b]:
            rank += 1
    total_rank.append(rank)

print(*total_rank)


