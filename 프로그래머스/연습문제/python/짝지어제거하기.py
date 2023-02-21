# 짝짓는 문제는 스택!
def solution(s):
    stack = []
    for i in  s:
        if len(stack) == 0: 
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    
    return 1 if len(stack) == 0 else 0


# 효율성 실패
def solution(s):
    answer = 0
    
    start = 0
    
    while start < len(s)-1:
        if s[start] == s[start+1]:
            if len(s) == 2:
                return 1
            s = s[:start] + s[start+2:]
            # print(s)
            start = max(0, start-1)
            
        else:
            start += 1
    

    return answer

