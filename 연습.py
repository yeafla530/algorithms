def find_min_cnt(idx, cnt):
    global ans 
    if cnt > 6:
        return
    
    if idx == len(blocks):
        if is_possible():
            ans = min(ans, cnt)
    
        return
    
    x, y = blocks[idx]

    gid[x][y] - '.'
    find_min_cnt(idx + 1, cnt + 1)
    frid[x][y] = '#'

    find_min(idx+1, cnt)