# 왜틀렸을까 
n, m, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
# 1행부터 시작
winds = [tuple(input().split()) for _ in range(q)]



def move(r, d):
    if d == "L":
        grid[r] = grid[r][-1:] + grid[r][:-1]
    else:
        grid[r] = grid[r][1:] + grid[r][:1]


for (r, d) in winds:
    r = int(r) - 1
    move(r, d)
    # r기점 위로
    c_d = d
    is_diff = True
    for i in range(r-1, -1, -1):
        c_d = "L" if c_d == 'R' else "R"
        # 하나라도 같은게 있으면 나오기
        for j in range(m):
            if grid[i+1][j] == grid[i][j]:
                # print("위")
                is_diff = False
                move(i, c_d)
                break
            else:
                is_diff = True

        if is_diff:
            break


    # r 기점 아래로
    d_d = d
    is_diff = True
    for i in range(r+1, n):
        d_d = "L" if d_d == 'R' else "R"
        for j in range(m):
            if grid[i-1][j] == grid[i][j]:
                # print("아래")
                is_diff = False
                move(i, d_d)
                break
            else:
                is_diff = True
                
        if is_diff:
            break



for i in range(n):
    print(*grid[i])