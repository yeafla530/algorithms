# n이 1000이하라는걸 보면 for문을 2번 돌리는거까진 괜찮겠다라는걸 아는게 중요
# 처음에 조건에 만족하는 수가 나오면 반복문을 바로 종료하는 식으로 짰는데
# 끝까지 돌려봐야하는 것이 포인트였다

# j 는 i ~ i+x까지
# 간단한 완전탐색 문제

# 두 곱의 합이 n이라면 1~sqrt(n)+1까지 돌리면 됨

import sys
from math import sqrt

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n, x = tuple(map(int, input().split()))
ans = INT_MAX

# 완전탐색을 진행합니다.
# 크기 순으로 i, j라 했을 때
# 차이가 x 이하인 경우 중
# n보다 크면서 가장 작은 값을 계산합니다.
sqn = int(sqrt(n))
for i in range(1, sqn + 2):
    # b는 (n / a) + 1보다 커야함
    j = max(i, n // i + 1)
    if j - i <= x:
        ans = min(ans, i * j)

print(ans)

# 두개의 수를 sqrt(n) + 1, sqrt(n) + 1로 잡았다면
# 정답이 되는 a, b 가 sqrt(n)+1보다 크더라도 
# 제일 최적의 답은 sqrt(n) + 1이될 수 밖에 없다
