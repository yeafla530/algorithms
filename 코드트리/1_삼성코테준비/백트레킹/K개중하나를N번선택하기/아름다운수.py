# 해당 숫자만큼 연달아 같은 숫자가 나오는 숫자를 아름다운 수라고 함
n = int(input())
seq = []
ans = 0

# 시작점을 고정시키고 for문으로 다음 숫자들 찾음
def is_beauty():
    i = 0 # 연달아 같은 숫자가 나오는 시작 위치
    while i < n:
        # 만약 해당 숫자만큼 나올 수 없으면 아름다운수가 아니다
        if i + seq[i] - 1 >= n:
            return False
        
        for j in range(i, i+seq[i]):
            if seq[j] != seq[i]:
                return False
            
        i += seq[i]

    return True


def choose(cnt):
    global ans
    if cnt == n:
        if is_beauty():
            ans += 1
        return
    
    for i in range(1, 5):
        seq.append(i)
        choose(cnt+1)
        seq.pop()



if n == 1:
    print(1)

else:

    choose(0)
    print(ans)