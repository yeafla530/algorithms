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