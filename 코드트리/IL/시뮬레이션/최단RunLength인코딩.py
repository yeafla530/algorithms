import sys
INT_MAX = sys.maxsize
s = list(input())
min_result = INT_MAX


def move_right():
    global s
    s = list(s[-1]) + s[:-1]

# 문자열 count
def count_string():
    global min_result
    # 글자 개수
    n = 1
    check = ''
    # 현재 string
    temp = s[0]

    for i in range(1, len(s)):
        # 만약 이전과 현재가 같다면
        if temp == s[i]:
            n += 1
        else:
            check += s[i-1] + str(n)
            
            temp = s[i]
            n = 1
    check += temp + str(n)
    # print(check)

    min_result = min(min_result, len(check))

# 한칸씩 앞으로 
for i in range(len(s)):
    count_string()
    move_right()


print(min_result)
    

