## 풀이가 다양하다!
# 일단 n이 작으면 어떻게 풀이도 만점이구나~ 생각하기
# 풀기만 하면 맞출 수 있음
# 1억이 1초 n이 10이면 8중 for문을 짜도 만점이란뜻!


#### 1. (i, j)를 잡는게 n^2 => 시작점
#### 2. (k, l)의 크기 잡는게 n^2 => 사각형 크기
#### 3. 사각형 안의 수돌아서 합 구하기 => n^2 
#### => 총 n^6 (10의 6승 => 100만) success/ (10의 8승이 1억)


#### n이 100이었다면 누적합 사용 
### IM단원에 누적합 배우기 => 누적합을 미리 만들면 미리 합을 구하는 
### 시간 복잡도가 N^2에서 1로 바뀜


#### 동적계획법까지 사용하는것은 더더욱 필요없는 풀이,,!
#### 최대연속수열합의 최대값을 2차배열로 생각해서 풀 수 있음 => O(n^3)



import sys

INT_MIN = -sys.maxsize

# 변수 선언 및 입력:
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
ans = INT_MIN


# 좌측상단 모서리의 위치를 (x1, y1)
# 우측하단 모서리의 위치를 (x2, y2)로 하는
# 직사각형 내 수들의 합을 반환합니다.
def get_score(x1, y1, x2, y2):
    sum_val = 0
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            sum_val += grid[i][j]
        
    return sum_val

   
# 모든 직사각형을 잡아보는
# 완전탐색을 진행합니다.
# 좌측상단 모서리의 위치를 (i, j)
# 우측하단 모서리의 위치를 (k, l)로 하는
# 직사각형을 전부 잡아봅니다.
for i in range(n):
    for j in range(n):
        for k in range(i, n):
            for l in range(j, n):
                ans = max(ans, get_score(i, j, k, l))

print(ans)
