def solution(A, B):
    answer = -1
    count = len(A)
    s = A
    
    for i in range(0, count):
        if s == B:
            answer = i
            break
        
        s = A[-1] + A[:-1]
        A = s
        # print(s)
        
    
    return answer