def check(queen, row):
    for i in range(0, row):
        if (queen[row] == queen[i] or abs(queen[row] - queen[i]) == row - i):
            return False
    return True

def search(queen, row):
    n = len(queen)
    count = 0
    if (n == row):
        return 1
    
    for col in range(0, n):
        queen[row] = col
        if (check(queen, row)):
            count += search(queen, row+1)
            
    return count

def solution(n):
    queen = [0 for _ in range(n)]
    return search(queen, 0)