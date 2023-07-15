# 대기업 문제 모음

> 백준 기준으로 대기업에서 나온 기출문제와 비슷한 문제 모음
>
> 정답비율 내림차순 순으로 풀이
>
> https://www.acmicpc.net/workbook/view/4357



## 1. 돌게임

url : https://www.acmicpc.net/problem/9655

### 내 풀이 (그리디)

* 그리디하게 최선의 선택으로 3개씩 가져갔을 때 횟수와 그 후 나머지 돌의 개수를 합해서 짝수인지 홀수인지에 따라 승패 결정

```python

n = int(input())

ans = n
moc = ans // 3
ans %= 3

if (moc + ans) % 2 == 0:
    print("CY")
else:
    print("SK")

```

### 유도 풀이 (수학, DP)

* 수학 - 짝수개면 창영이가 이기고, 홀수개면 상근이가 이김

```python
n = int(input())

if n%2==0:
    print('CY')
else:
    print('SK')
```

* DP
  * 타블레이션 기법을 사용 (바텀업)
  * i개의 돌을 가지고 있는 경우 누가 이기는지 체크하고, 현재 위치에서 1개, 3개를 가져갔던 사람을 체크
  * 현재 돌보다 1개 적었을 때 상근이가 이겼으면 다음번엔 창영이가 이기고, 현재 돌보다 3개 적었을 때 상근이가 이겼을 때도 다음번엔 창영이가 이길 수 있다

```python
n = int(input())
dp = [-1] * 10001

dp[1] = 0 # SK
dp[2] = 1 # CY
dp[3] = 0 # SK

for i in range(4, n+1):
    if dp[i-1] == 0 or dp[i-3] == 0:
        dp[i] = 1
    else:
        dp[i] = 0

# print(dp)
if dp[n]:
    print("CY")
else:
    print("SK")
```

