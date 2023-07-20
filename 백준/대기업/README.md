# 대기업 문제 모음

> 백준 기준으로 대기업에서 나온 기출문제와 비슷한 문제 모음
>
> 정답비율 내림차순 순으로 풀이
>
> https://www.acmicpc.net/workbook/view/4357



## 1. 9655 돌게임

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



## 2. 25757 임스와 함께하는 미니게임

https://www.acmicpc.net/problem/25757

### 내 풀이 (반복문) - 시간초과

* array에서 해당 player를 찾는 과정 N이 추가되어 총 O(N^2)의 시간복잡도를 거친다

```python
n, play = input().split()
n = int(n)
already = []
ans = 0
cnt = 0

for i in range(n):
    player = input()

    if player not in already:
        cnt +=1
    
    if play == "Y" and cnt == 1:
        ans += 1
        cnt = 0
    elif play == "F" and cnt == 2:
        ans += 1
        cnt = 0
    
    elif play == "O" and cnt == 3:
        ans += 1
        cnt = 0
    
    if player not in already:
        already.append(player)


print(ans)
```



### 유도 풀이 (set)

* 반복되는 플레이어를 없애면 되는 것이므로 자료구조 set을 사용해 중복을 없앤다

```python
d = {"Y": 1, "F": 2, "O": 3}
n, play = input().split()
player = [input() for _ in range(int(n))]
player = list(set(player))

ans = len(player) // d[play]

print(ans)
```



## 3. 2631 줄세우기

https://www.acmicpc.net/problem/2631

* 정답률이 65퍼인데 왜 감도 오지 않는가



### 다른사람 풀이

* 전형적인 위상정렬 문제
* A번 학생이 B번 학생보다 반드시 먼저 앞에 와야하는 상황이 주어지기 때문에
* A -> B를 만족시키면서 정렬을 해야하기 때문









## 4. 15989 1, 2, 3 더하기 4

https://www.acmicpc.net/problem/15989

### 내 풀이 - 틀림

* 1을 전부 

```
n = int(input())
for _ in range(n):
    num = int(input())
    dp = [0] * 10001

    dp[0] = 1
    numbers = [1, 2, 3]
    for i in range(1, num+1):
        for j in range(3):
            if i >= numbers[j]:
                dp[i] = (dp[i] + dp[i - numbers[j]])
        
    
    print(dp[num])
```



