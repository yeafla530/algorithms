s = list(input())
s.reverse()

is_zero = True
for i in range(len(s)):
    # 만약 0보다 큰수가 안나오는 경우
    if is_zero and s[i] == '0':
        continue
    # 0보다 큰수가 나오는 경우
    is_zero = False
    print(s[i], end="")