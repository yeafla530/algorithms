n = int(input())
arr = list(map(int, input().split()))
mid = []


for i in range(n):
    if (i+1) % 2:
        mid = sorted(arr[:i+1])
        cnt = len(mid)
        # print(mid, cnt)

        idx = cnt // 2
        print(mid[idx], end=" ")
        
