from collections import deque
def solution(people, tshirts):
    # 한사람당 최대 하나
    # 모든 참가자는 자신의 상의 크기와 같거나 큰 티셔츠 받음
    answer = 0

    # 정렬 
    people.sort()
    tshirts.sort()
    people = deque(people)
    # 티셔츠를 나눠줌

    first = people.popleft()
    for item in tshirts:
        # print(people, item, first, answer)
        if first <= item:
            # print(people)
            answer += 1
            if (len(people)):
                first = people.popleft()
            else:
                break
        else:
            continue



    return answer