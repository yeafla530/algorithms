def solution(n):
    if n == 1:
        return [[1]]
    answer = [[0 for _ in range(n)] for _ in range(n)]
    
    i, j = 0, 0
    dir = 'r'
    for cnt in range(1, n*n+1):
        answer[i][j] = cnt
        
        if dir == 'r':
            j += 1
            if j == n-1 or answer[i][j+1] != 0:
                dir = 'd'
            
        elif dir == 'd':
            i += 1
            if i == n-1 or answer[i+1][j] != 0:
                dir = 'l'
        
        elif dir == 'l':
            j -= 1
            if j == 0 or answer[i][j-1] != 0:
                dir = 'u'
        
        else:
            i -= 1
            if i == 0 or answer[i-1][j] != 0:
                dir = 'r'
                
    # for i in range(n):
    #     for j in range(n):
    #         print(answer[i][j], end=" ")
    #     print()
    return answer