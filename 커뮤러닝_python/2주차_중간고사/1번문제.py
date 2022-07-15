# from collections import deque
def solution(booked, unbooked):
    # 예약 고객 업무를 일반고객보다 먼저 처리
    # 1. 예약 고객 중 먼저 도착한 고객 업무 먼저 처리
    # 2. 예약고객 없으면 먼저 도착한 일반 고객
    # 3. 시작한 업무는 중간에 중단하지 않음 -> 중간에 예약 고객이 와도 끝내고 예약 고객처리 

    # hh:mm => 00:01 ~ 23:50
    # 도착시간 같은 고객 x
    answer = []
    lst = []
    for item in booked:
        item.append('booked')
        lst.append(item)
    for x in unbooked:
        x.append('unbooked')
        lst.append(x)

    lst.sort(key = lambda x: x[0])

    # 초기 시, 분 설정
    hour, minute = map(int, lst[0][0].split(':'))
    answer.append(lst[0][1])
    stack = []
    minute += 10
    # 10분 추가
    for i in range(1, len(lst)):
        print(minute)
        if (minute // 60 != 0):
            minute -= 60
            hour += 1

        new_hour, new_minute = map(int, lst[i][0].split(':'))
        # 10분이 넘어가기 전 중간에 온 사람들
        if ((new_hour == hour and new_minute <= minute) or (new_hour < hour)):
            # 예약한 사람이 왔으면 PUSH
            if (lst[i][2] == 'booked'):
                # print('book')
                minute += 10
                answer.append(lst[i][1])
            else:
                # print('unbook')
                stack.append(lst[i][1])

        # 없으면 stack에 담은 사람들 push
        else:
            while len(stack) != 0:
                answer.append(stack[0])
                stack.pop(0)

        # print(answer, stack)

    if (len(stack)):
        while len(stack) != 0:
                answer.append(stack[0])
                stack.pop(0)

    if (len(answer) != len(lst)):
        for item in lst:
            if not item[1] in answer:
                answer.append(item[1])

    return answer