# 꽤 어려움 
# DP로 풀어야할 때 
# 개선된 완전탐색 풀이 생각해내기 힘들었다
# 문자열을 순회하며 문자열의 중심일 때를 가정하여 확장해 나간다
st = input()
ans = 0

def get_max_palindrome_length(start, end):
    # 문자열 범위를 벗어나지 않으면서 좌우가 대칭인 경우 확장함
    while start >= 0 and end < len(st) and st[start] == st[end]:
        # print(st[start], st[end], start, end)
        start -= 1
        end += 1
    
    # print()
    
    # while문 끝났을 때 start와 end는 각각 좌우가 대칭이 깨진 첫 문자의 인덱스를
    # 가리키고 있기때문에 이를 보정해준다
    start += 1
    end -= 1

    return end - start + 1


# 홀수개
for center in range(len(st)):
    ans = max(ans, get_max_palindrome_length(center, center))

# 짝수개
for center in range(len(st)-1):
    ans = max(ans, get_max_palindrome_length(center, center+1))

print(ans)

###################################################
# DP 풀이 - 타블레이션
# 꽤 어려움 
# DP로 풀어야할 때 어려워!!!
# start부터 end까지 부분 문자열 좌우대칭인지 여부
st = input()
ans = 0

dp = [[False]*len(st) for _ in range(len(st))]

# 초기조건 1 : 단일 글자의 경우
for i in range(len(st)):
    dp[i][i] = True

# 초기조건 2 : 연속된 두 글자가 일치하는 경우
for i in range(len(st)-1):
    dp[i][i + 1] = (st[i] == st[i+1])

# 점화식
# 글자 수 3 ~ n까지
for str_len in range(3, len(st)+1):
    # 일단 원하는 글자수의 양쪽 끝을 잡는다 (start, end)
    for start in range(len(st) - str_len + 1):
        end = start + str_len - 1
        # 이전 비교 값이 true고 현재 양쪽 string이 같은경우 True 
        if dp[start+1][end-1] and st[start] == st[end]:
            dp[start][end] = True

# 모든 부분 문자열에 대해 좌우대칭인지 확인후
# 가장 긴 좌우대칭인 부분 문자열 저장
for start in range(len(st)):
    for end in range(start, len(st)):
        if dp[start][end]:
            ans = max(ans, end - start + 1)

print(ans)

###################################
# 메모이제이션 답
# 메모리 초과남;;
# 메모이제이션 풀이
# DP[start][end] = 문자열의 start부터 end까지의 부분 문자열 좌우대칭인지 여부

st = input()
ans = 0

dp = [[-1]*len(st) for _ in range(len(st))]


def is_palindrome(s, e):
    if s == e:
        return True
    
    if s == e + 1:
        return st[s] == st[e]

    # 메모이제이션
    if dp[s][e] != -1:
        return dp[s][e]
    
    # dp가 -1인 경우 (처음 체크할때)
    # 이전 양쪽값, 현재 양쪽값 확인
    dp[s][e] = is_palindrome(s+1, e-1) and st[s] == st[e]
    return dp[s][e]


for start in range(len(st)):
    for end in range(start, len(st)):
        if is_palindrome(start, end):
            ans = max(ans, end - start + 1)

# print(dp)
print(ans)

