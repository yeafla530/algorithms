# n 10^9이기 떄문에 hashmap 사용
# 시간을 커팅하려 노력하기
# key순서를 보장하려면 파이썬 3.6 이상부터 가능하다
# 원래는 입력순서대로 보장이 안되었는데 이제 된다~

###### 완탐이용하면 n^2 => 시간초과
# 변수 선언 및 입력:
n = int(input())
arr = list(map(int, input().split()))
   
# 완전탐색을 이용하여
# 각 수마다 몇 번씩 등장했는지를 확인합니다.
ans = -1
for i in range(n):
    cnt = 0 # arr[i]가 몇 번 등장하는지 살펴봅니다.
    for j in range(n):
        ## 커팅하기
        if cnt == 2:
            break
        # TC : 1 2 3 4 ... 4 3 2 1 처럼 대칭인 경우
        # 최악의 시간이 나옴
        if arr[j] == arr[i]:
            cnt += 1

    
    # 정확히 1번만 등장한다면
    # 답이 됩니다.
    if cnt == 1:
        ans = arr[i]
        break

print(ans)
