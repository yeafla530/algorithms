s, e = map(int, input().split())

cnt = 0
for i in range(s, e+1): 
    sum_num = 0
    # 약수 구하기
    for j in range(1, i):
        if i % j == 0:
            sum_num += j
    
    if sum_num == i:
        cnt += 1

print(cnt)