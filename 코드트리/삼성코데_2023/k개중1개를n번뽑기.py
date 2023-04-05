# n자리 수 2진수 만들기

n = 3
answer = []


def choose(cnt):
    if cnt == n:
        print_answer()
        return

    for i in range(2):
        answer.append(i)
        choose(cnt+1)
        answer.pop()

choose(0)