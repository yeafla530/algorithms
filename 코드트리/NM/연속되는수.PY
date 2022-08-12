# 나의 풀이
n = int(input())
pre = 0
max_cnt = 1
cnt = 1
for i in range(n):
    a = int(input())
    
    if i == 0:
        pre = a
    
    else:
        if a == pre:
            cnt += 1
            # print(cnt)  
        else:
            if max_cnt < cnt:
                max_cnt = cnt
            cnt = 1
            pre = a
    # print(pre)
if max_cnt < cnt:
    max_cnt = cnt
print(max_cnt)


# 풀이
n = int(input())
arr = [int(input()) for _ in range(n)]

ans, cnt = 0, 0

for i in range(n):
    if i >= 1 and arr[i] == arr[i-1]:
        cnt += 1
    else:
        cnt = 1
    
    ans = max(ans, cnt)

print(ans)