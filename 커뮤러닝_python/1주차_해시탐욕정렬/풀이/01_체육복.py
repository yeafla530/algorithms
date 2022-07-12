# 방법 1 => O(n)
def solution(n, lost, reserve):
    student = {}
    # 초기화
    for i in range(n+2):
        student[i] = 1
    for x in reserve:
        student[x] += 1
    for y in lost:
        student[y] -= 1
    
    for (k, v) in student.items():
        if (v == 0):
            if (student.get(k-1) == 2):
                student[k] += 1
                student[k-1] -= 1
            elif (student.get(k+1) == 2):
                student[k] += 1
                student[k+1] -= 1
    cant_play = [v for (k, v) in student.items() if v < 1]
    return n - len(cant_play)
    
    
# 방법 1 - 강사님 풀이
def solution(n, lost, reserve):
    u = [1] * (n + 2)
    for i in reserve:
        u[i] += 1
    for i in lost:
        u[i] -= 1
    
    # 학생수만큼 반복
    for i in range(1, n+1):
        # 현재 학생이 체육복이 2개고 앞에 사람을 빌려줄 수 있으면
        if u[i] == 2 and u[i-1] == 0:
            u[i-1:i+1] =  [1, 1]
        elif u[i] == 2 and u[i+1] == 0:
            u[i:i+2] = [1, 1]
    
    return len([x for x in u[1:-1] if x > 0])


def solution(n, lost, reserve):
    # 체육복 가져왔는데 도난당한 학생 (교집합)
    s = set(lost) & set(reserve)
    # 잃어버린 학생
    l = set(lost) - s
    # 가져왔는데 도난안당한 학생들
    r = set(reserve) - s

    # 집합 R만큼 반복, 정렬하는데 O(klogk)
    for x in sorted(r):
        # x에는 체육복을 빌려줄 수 있는 학생들
        if x - 1 in l:
            l.remove(x - 1)
        elif x + 1 in l:
            l.remove(x + 1)
        
    # 빌리지 못한 학생
    return n - len(l)    

