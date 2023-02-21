def solution(A,B):
    answer = 0
    # 누적값이 최소
    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        answer += A[i] * B[i]
    

    return answer