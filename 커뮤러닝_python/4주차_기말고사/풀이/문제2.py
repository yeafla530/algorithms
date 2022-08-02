from collections import defaultdict
from heapq import heappush
from heapq import heappop

def solution(s1, s2, k):
    if k not in s2:
        return [k]
    answer = []

    # 바닥 과목 찾는 편의를 위해 hash등록
    dic = defaultdict(list)
    # 수강 조건 확인을 위한 hash
    possible = defaultdict(int)
    prev = defaultdict(list)

    for a, b in zip(s1, s2):
        dic[b].append(a)
        possible[b] += 1
        prev[a].append(b)
    
    # 바닥 찾기
    stack = []
    stack += dic[k]
    bottom = []
    check = set([]) # 중복처리 검사용

    while stack:
        lecture = stack.pop()
        if lecture in check: continue
        check.add(lecture)
        if lecture in dic:
            stack += dic[lecture]

        else:
            if lecture in bottom: continue
            heappush(bottom, lecture)

    
    print(bottom, stack, check)


    # 원하는 과목까지 반복
    while True:
        # 바닥중 빠른순서 수강
        lecture = heappop(bottom)
        answer.append(lecture)

        # 선수과목 조건처리
        for x in prev[lecture]:
            possible[x]-=1
            # 답이 나온 경우
            if possible[x] == 0 and x == k:
                print(answer + [k])
                return answer+[k]
            # 수강하면서 새로 열린 과목 바닥에 추가, 수강 원하는 과목 뿌리에서만
            if possible[x] == 0 and (x in check):
                heappush(bottom, x)

    

solution(["A","E","B","D","B","H","F","H","C"], ["G","C","G","F","J","E","B","F","B"], "B")
solution(["A","E","B","D","B","H","F","H","C"], ["G","C","G","F","J","E","B","F","B"], "G")


