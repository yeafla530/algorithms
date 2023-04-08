# n자리 2진수중 0이 인접해서 등장하지 않는 수만 구해 출력하는 코드
# 0을 추가하기 위한 조건 넣어주기

n = 3
answer= []


def choose(cnt):
    if cnt == n:
        print(*answer)
        return

    if cnt == 0 or answer[-1] != 0:
        answer.append(0)
        choose(cnt+1)
        answer.pop()

    answer.append(1)
    choose(cnt+1)
    answer.pop()
            


choose(0)

# 연속하여 같은 숫자 나오지 않도록 함
k, n = 5, 3
answer = []

def choose(cnt):
    if cnt == n:
        print(*answer)
        return

    for i in range(1, k+1):
        if cnt >= 2 and i == answer[-1] and i == answer[-2]:
            continue
        
        answer.append(i)
        choose(cnt+1)
        answer.pop()

choose(0)
