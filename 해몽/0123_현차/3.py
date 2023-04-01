import sys
si = sys.stdin.readline
MOD = 1000000007
dy = [[0 for _ in range(10)] for _ in range(100005)]  # dy[i][k] := i 자리 수 중에서 k 로 시작하는 안전한 수 개수
def preprocess():
    # Initial Value
    for num in range(10):
        dy[1][num] = 1  # safe itself 
    
    # Dynamic
    for len in range(2, 100001):
        for num in range(10):
            for next_num in range(10):
                if num != 4:
                    dy[len][num] += dy[len - 1][next_num]
                    dy[len][num] %= MOD
                elif next_num != 7:
                    dy[len][num] += dy[len - 1][next_num]
                    dy[len][num] %= MOD


def solve(N): # Count the safe number equal or below than N
    L = len(N)
    left_length = L
    ret = 0

    for idx in range(L + 1): # idx번째 숫자를 보고있다
        if idx >= 2 and N[idx-2] == "4" and N[idx-1] == "7": # 이미 ~~47까지 그룹핑된 상황 전부 무시
            break
            
        if idx == L:
            ret += 1
        
        cur = int(N[idx]) # cur이 해당 위치에 적혀있는 숫자
        for num in range(0, cur):
            # 7로 시작하는 그루핑으로 시작하는데 앞의 수가 4면 제외
            if num == 7 and idx >= 1 and N[idx-1] == "4":
                continue
            if num < cur:
                ret += dy[left_length][num]
                ret %= MOD
        left_length -= 1

    return (ret + MOD - 1) % MOD # 0을 다시 안전한 수에서 제외하기

T = int(si())
for _ in range(T):
    N = int(si())
    print(solve(N))
