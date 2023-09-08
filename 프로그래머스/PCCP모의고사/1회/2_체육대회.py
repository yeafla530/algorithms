# 여러종목에 대해 각 반의 해당 종목 대표 1명씩 나와 대결
# 한 학새은 최대 1개 종목만 대표
# 한 종목당 1명의 대표 뽑으려고함
# 각 종목 대표의 해당 종목에 대한 능력치의 합 최대화하는 것

answer = 0

def DFS(l, s, ability, check):
    global answer
    # n = 학생수 m = 종목수
    n = len(ability)
    m = len(ability[0])
    
    if l == m:
        answer = max(answer, s)

    
    else:
        for i in range(n):
            if check[i] == 0:
                check[i] = 1
                DFS(l+1, s + ability[i][l], ability, check)
                check[i] = 0



def solution(ability):
    global answer
    check = [0] * len(ability)
    DFS(0, 0, ability, check)
    # Level, sum, ability, check
    # Level : 고를 수 있는 학생수 중 몇명째 선택할 것인지
    
    
    return answer