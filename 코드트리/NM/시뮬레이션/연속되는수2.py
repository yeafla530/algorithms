n = int(input())

before = int(input())
max_cnt = 1
cnt = 1
for _ in range(n-1):
    num = int(input())

    if before == num: 
       cnt += 1
    else:
        cnt = 1
    
    before = num

    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)