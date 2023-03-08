k, n = map(int, input().split())
arr = []

# cnt번째 자리 숫자 결정
def select(a):
    # 종료조건
    # 횟수n 넘으면
    if a == n+1:
        print(*arr)
        return
    # 재귀호출
    # 1부터 시작해서 사전순으로 정렬됨
    for i in range(1, k+1):
        # i를 위한 연산
        arr.append(i)
        select(a+1)
        # i에 대한 역 연산
        arr.pop()


select(1)

# 내풀이
k, n = map(int, input().split())
answer = []

def choose(cnt):
    if cnt == n:
        print(*answer)
        return 

    for i in range(1, k+1):
        answer.append(i)
        choose(cnt+1)
        answer.pop()


choose(0)