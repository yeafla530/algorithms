import sys
si = sys.stdin.readline

# 카드의 수, 시작 숫자
n, s, m = map(int, si().split())
cards = []

for _ in range(n):
    value, equation = si().split()
    cards.append([int(value), equation])


ans = s
used = [False for _ in range(n)]

def apply(val, equation):
    if equation[0] == '+':
        return val + int(equation[1:])

    else:
        return val * int(equation[1:])



# 재귀함수 사용하기
def func(val, money): # 현재 가지고있는 수 val와 money
    global ans
    ans = max(ans, val)


    for i in range(n):
        if used[i]: # 이미 사용한 카드면 시도하지 않는다
            continue
        
        if cards[i][0] > money: # 예산을 넘어서는 카드는 사용하지 않는다
            continue

        used[i] = True
        func(apply(val, cards[i][1]), money - cards[i][0])
        used[i] = False



func(s, m)
print(ans)

'''
5 5000 10000
1000 +10
5000 *3
3200 *5
4200 *5
3200 +10

=> 125250
'''


'''
3 1 50
20 +30
10 *10
5 *100

'''