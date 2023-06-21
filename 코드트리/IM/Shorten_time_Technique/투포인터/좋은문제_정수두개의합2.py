n, k = map(int, input().split())
# 2중 for문은 힘들다
arr = [0]
for _ in range(n): 
    arr.append(int(input()))

##### 중요
arr.sort()

ans = 0

j = n
# i는 1부터 n까지 증가시키기
# arr[i] + arr[j] <= k를 만족하는 j중 최대의 j가 잡히도록 tow pointer진행할 수 있다
for i in range(1, n+1):
    # 투포인터의 정의 : 두개의 포인트를 잡아 이동한다

    while j != i and arr[i] + arr[j] > k:
        j -= 1    

    
    if j <= i:
        break

    
    ans += j-i


print(ans)