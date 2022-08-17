# 원소들의 평균값이 그 구간의 원소 중 하나가 되는 서로 다른 가짓수
n = int(input())
arr = list(map(int, input().split()))

all_cnt = 0
# 전체 구간
for i in range(n):
    # n개의 구간
    for j in range(i, n):
        s = 0
        cnt = 0
        avg = 0
        elems = []
        for k in range(i, j+1):
            s += arr[k]
            elems.append(arr[k])
            cnt += 1
        avg = s / cnt
        # print(elems, avg)
        if avg in elems:
            all_cnt += 1

print(all_cnt)

    
