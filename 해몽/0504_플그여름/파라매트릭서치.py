l, r, ans = 0, 100, 1000

while l <= r:
    # 중간값 구하기
    mid = (l + r) // 2  

    # 숙제 성공가능
    if solve(mid):
        ans = mid
        r = mid - 1
    
    else:
        l = mid + 1

print(ans)