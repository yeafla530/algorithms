def solution(n):
    # 5억까지 있기때문에 for문은 불가하다
    # 3진수와 방법은 동일
    # index로 인해 1을 빼고 진행
    answer = ''
    lst = ['1', '2', '4']
    
    while n > 0:
        n = n-1
        answer += lst[n%3]
        n = n // 3
    
    
    
    
    return answer[::-1]