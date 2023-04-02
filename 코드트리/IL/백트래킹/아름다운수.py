def count_beautiful_seq(cnt):
    global ans
    # 종료조건
    if cnt >= n:
        # 길이만 가지고 
        if cnt == n:
            ans += 1
        return
    # n자리수 만큼 반복할 수 있는 것은 n이하의 수
    for i in range(1, 5):
        seq.append(i)
        # 길이를 이용해라,,?
        count_beautiful_seq(cnt + i)
        seq.pop()


count_beautiful_seq(0)
print(ans)

# 해당숫자만큼 연달아 같은 숫자가 나옴
# n자리 아름다운 수의 개수

n = int(input())
seq = []
ans = 0

####### O(K^n * n) => O(n)으로 줄이기
####### 끝나고 아름다운 수인지 확인하지 말고 백트레킹 실행할 때마다 체크하기
# def is_beautiful():
#     i = 0
#     while i < n:
#         # 만약 연속하여 해당 숫자만큼 나올 수 없다면 
#         # 아름다운 수가 아니다
#         # 현재 index(i)에 있는 값(seq[i])가 seq[i]번 반복해서 나타나야 아름다운 수
#         # 자기 자신을 제외한(-1) 인덱스가 마지막 index를 넘는다면 false
#         if i + seq[i] - 1 >= n:
#             return False
#         for j in range(i, i + seq[i]):
#             if seq[j] != seq[i]:
#                 return False
        
#         i += seq[i]
    
#     return True

###### 더 깔끔하게




###### cnt를 이용 => cur_num 숫자가 나온 횟수만큼 + 1 해주기
###### => O(K^N)
def count_beautiful_seq(cnt):
    global ans
    # 종료조건
    if cnt >= n:
        # 길이만 가지고 
        if cnt == n:
            ans += 1
        return
    # n자리수 만큼 반복할 수 있는 것은 n이하의 수
    for i in range(1, 5):
        seq.append(i)
        # 길이를 이용해라,,?
        count_beautiful_seq(cnt + i)
        seq.pop()


count_beautiful_seq(0)
print(ans)