n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
seq = [0 for _ in range(n)]

# 행 세기
def is_happy_seq():
    cnt = 1
    max_cnt = 1 
    for i in range(n-1):
        if seq[i] == seq[i+1]:
            cnt += 1
        else:
            cnt = 1
        
        max_cnt = max(max_cnt, cnt)
    
    return max_cnt >= m


# 행
ans = 0
for i in range(n):
    seq = arr[i][:]

    if is_happy_seq():
        ans += 1

for j in range(n):
    for i in range(n):
        seq[i] = arr[i][j]
    if is_happy_seq():
        ans += 1

print(ans)

