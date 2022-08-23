# n번 턴
# m개 판
# k개의 말
n, m, k = map(int, input().split())
turn = list(map(int, input().split()))
score = [1] * k
ans = 0

def calc():
    cnt = 0
    for s in score:
        cnt += (s >= m)
    return cnt

def choose(cnt):
    global ans
    # 말을 직접 n번 움직이지 않아도
    # 최대가 될 수 있으므로 항상 답 갱신
    ans = max(ans, calc())
    if cnt == n:
        return
    
    for i in range(k):
        score[i] += turn[cnt]
        choose(cnt+1)
        score[i] -= turn[cnt]


choose(0)
print(ans)
