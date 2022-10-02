# 꽤 사골문제
# a ( * ) => *를 a만큼 반복해라
# 중첩등장 가능 
# 3(r2(h)s)라면 rhhsrhhsrhhs로 복원가능


def solution(compressed):
    # S라는 문자열이 K번 반복될 때 K(S)로 나타낸다
    answer = ''
    stack = []
    idx = 0


    number = ''
    string = ''
    
    right = False
    def push(n, s):
        if len(n):
            return int(n)
        
        if len(s):
            return s

    while idx < len(compressed):
        if len(string) and (compressed[idx].isdigit() or not right):
            answer += string
            string = ''

        if compressed[idx].isdigit():
            number += compressed[idx]
        

        elif compressed[idx].isalpha():
            string += compressed[idx]

        elif compressed[idx] == '(':
            right = True
            x = push(number, string)
            stack.append(x)
            number = ''
            string = ''
        
        elif compressed[idx] == ')':
            print(right)
            if not right and len(stack):
                n = stack.pop()
                answer = (n * answer)

            if right:
                n = stack.pop()
                answer += (n * string)
                

            number = ''
            string = ''    
            right = False

        print(answer, stack, string, right)
        idx += 1
        

            
        
    return answer


solution("2(3(hi)co)")
