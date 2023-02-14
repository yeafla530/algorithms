n = int(input())
arr = list(map(int, input().split()))

ans = -987654321
sum_num = 0
for num in arr:
    if sum_num < 0:
        sum_num = num 
    else:
        sum_num += num

    ans = max(ans, sum_num)

print(ans)