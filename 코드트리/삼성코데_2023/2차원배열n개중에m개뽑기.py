ans = 0 

def find_min_cnt(idx, cnt):
    global ans

    if cnt > 6:
        return

    if idx == len(blocks):
        if is_possible():
            ans = min(ans, cnt)
        return

    x, y = blocks[idx]

    grid[x][y] = '.'
    find_min_cnt(idx+1, cnt+1)
    grid[x][y] = '#'


find_min_cnt(0, 0)