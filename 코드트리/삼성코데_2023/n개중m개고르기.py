# n자리 이진수중 1의 개수가 정확히 m개인 수만 구해 출력하는 코드
n, m = 3, 2 
answer = []


def choose(cur_num):
    if cur_num == n:
        cnt = 0
        for elem in answer:
            if elem == 1:
                cnt += 1
        if cnt == m:
            print(*answer)
        return

    answer.append(0)
    choose(cur_num+1)
    answer.pop()

    answer.append(1)
    choose(cur_num+1)
    answer.pop()


choose(0)

answer2 = []
def choose2(cur_num, cnt): # 지금까지 선택한 1의 개수가 cnt개라 했을 때
    # cur_num번째 위치에 0 또는 1을 선택하는 함수
    if cur_num == n+1:
        if cnt == m:
            print(*answer2)
        return
    answer2.append(0)
    choose2(cur_num+1, cnt)
    answer2.pop()

    answer2.append(1)
    choose2(cur_num+1, cnt+1)
    answer2.pop()

choose2(1, 0)