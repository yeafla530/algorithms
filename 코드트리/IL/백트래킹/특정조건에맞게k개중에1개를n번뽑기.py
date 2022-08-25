k, n = map(int, input().split())
arr = []
# 연속하여 같은 숫자가 3번 이상 나오면 안됨
# cnt번째 자리에 1 ~ K중에 선택
def choose(cnt):
    # 종료조건
    if cnt == n+1:
        print(*arr)
        return 
    # 재귀호출
    for i in range(1, k+1):
        # 만약 앞에 두개의 숫자가 없거나, 앞 두개 숫자와 지금 정하려는 숫자가 같은 경우가 아닐때 
        if cnt < 3 or not (i == arr[-1] and i == arr[-2]):
            arr.append(i)
            choose(cnt+1)
            arr.pop() 

choose(1)