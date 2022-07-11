def solution(n, lost, reserve):
    # 번호 체격순
    # 바로 앞번호 학생이나 뒷번호의 학생한테만 빌려줄 수 있음
    # 4번은 3번, 5번 양쪽에게 체육복 빌려줄수있음
    # 최대한 많은 학생이 체육수업 들어야함

    answer = n
    # set 차집합 
    new_lost = list(set(lost) - set(reserve))
    new_reserve = list(set(reserve) - set(lost))
    # print(new_lost, new_reserve)
    # 여벌 체육복 가져온 학생이 도난당했을 수도있음 => 제외시킴 
    for item in new_lost:
        upNum = item + 1
        downNum = item - 1
        # print(item)
        # print(downNum in new_reserve)
        if downNum in new_reserve:
            # print(downNum)
            new_reserve.remove(downNum)

        elif upNum in new_reserve:
            # print(upNum)
            new_reserve.remove(upNum)
        else:
            answer -= 1


    return answer