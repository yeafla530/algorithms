n, m = map(int, input().split())
answer = []

# 해설 풀이
# 몇개 들어있는지

# m개 숫자 골라 만들 수 있는 조합
def choose(num, cnt):
    if num == n+1:
        if cnt == m:
            print(*answer)
        return
    
    answer.append(num)
    choose(num+1, cnt+1)
    answer.pop()

    choose(num+1, cnt)




choose(1, 0)