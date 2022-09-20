def solution(board, skill):
    # O(n^4)
    answer = 0
    # type 1 : 공격, 2 : 회복
    # [type, r1, c1, r2, c2, degree]
    for s in skill:
        ty, r1, c1, r2, c2, degree = s
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if ty == 1:
                    board[i][j] -= degree
        
                else:
                    board[i][j] += degree
                
    cnt = 0
    # print(board)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 0:
                cnt += 1
    return cnt