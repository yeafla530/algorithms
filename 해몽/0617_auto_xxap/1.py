# 슬라이딩 윈도우
import sys

si = sys.stdin.readline
n, m = map(int, si().split())
a = list(map(int, si().split()))
unique = [False for _ in range(m)]

cnt = [0 for _ in range(n+1)]
redudant_cnt = 0


# 창문을 놓을 수 있는 모든 위치에 대해서 중복 여부 판단하기, O(M)
for i in range(m+n-1): # 창문의 오른쪽 끝이 i번째에 있는 상황
    if i < m:
        # i번지는 이번에 새롭게 창문에 들어온 친구
        cnt[a[i]] += 1   # i번지에 적힌 수(a[i])의 개수를 1개 증가
        if cnt[a[i]] == 2: # 만약 증가시켜놨는데 2개 등장한다면?
            redudant_cnt += 1 # 새롭게 중복되는 수가 등장
    
    if i >= n:
        # i-n번째는 이번에 창문에서 빠지는 친구
        cnt[a[i-n]] -= 1        # i-n번째에 적힌수 (a[i-n])의 개수를 1개 감소
        if cnt[a[i-n]] == 1:    # 만약 감소시켜놨는데 1개 등장한다면?
            redudant_cnt -= 1   # 중복이던 수가 유일한 수로 바뀜

    if redudant_cnt == 0 and i >= n-1: # 만약 창문에 중복이 없다면
        unique[i-n+1] = True           # (i-n+1)번째에서 시작하는 창문은 중복이 없다
    


# 각 설치 방법에 대해서 가능여부 판단하기, O(M)
cnt = [0 for _ in range(n+1)]
prefix_uniqueness = True # 첫번째 창문에 중복이 존재하는가?

for i in range(n): # 0~i번지에 창문을 설치하기 시작
    cnt[a[i]] += 1
    if cnt[a[i]] == 2:
        prefix_uniqueness = False
    
    postfix_uniquness = True # 두번째 창문부터 계속해서 창문을 설치했을 때 중복이 있는가?
    s = i + 1

    while s < m:
        postfix_uniquness = postfix_uniquness & unique[s]
        s += n

    if postfix_uniquness and prefix_uniqueness:
         print("Y", end="")
    
    else:
        print("N", end="")

'''
4 9
3 1 4 2 3 2 1 4 3
=>
YNNY
'''