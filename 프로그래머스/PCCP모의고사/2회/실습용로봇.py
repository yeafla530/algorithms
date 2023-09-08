def solution(command):
    answer = []
    x, y = 0, 0
    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]
    # 방향
    d = 0
    
    for elem in list(command):
        if elem == 'G':
            x = x + dxs[d]
            y = y + dys[d]
            
        elif elem == 'B':
            x = x - dxs[d]
            y = y - dys[d]
            
        elif elem == 'R':
            d = (d+1) % 4
        else:
            d = (d-1+4) % 4
            
               
    
    
    
    return [x, y]