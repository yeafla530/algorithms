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

# 김진환님 풀이
def addMinutes(time:str, minutes:int)->str: # 시간 경과 함수
    t_hour, t_minutes = map(int, time.split(':'))
    t_minutes += minutes
    if t_minutes >= 60: # 60분 이상인 경우 시간으로 변환
        t_hour += 1
        t_minutes -= 60
    return ':'.join([str(t_hour).zfill(2), str(t_minutes).zfill(2)]) # zfill 을 통해서 문자열의 자리 수를 0으로 채움

def solution(booked:list, unbooked:list)->list:
    answer = []

    previous_completion_time = "" # 이전 상담 완료 시간
    while(booked and unbooked): # 예약 고객과 비예약 고객이 모두 존재하는 경우에만 반복
        current_customer_info = list()

        # 상담 고객 선택
        if booked[0][0] <= previous_completion_time: # 이전 상담 완료 시각보다 먼저 도착한 예약 고객 선택
            current_customer_info = booked.pop(0)
        elif unbooked[0][0] <= previous_completion_time: # 이전 상담 완료 시각보다 먼저 도착한 비예약 고객 선택
            current_customer_info = unbooked.pop(0)
        else: # 이전 상담 완료 시각 이후 가장 먼저 도착한 고객 선택
            if booked[0][0] <= unbooked[0][0]: # 예약 고객과 비예약 고객 시간 비교
                current_customer_info = booked.pop(0)
            else:
                current_customer_info = unbooked.pop(0)

        # 상담 시작 시간 계산
        if previous_completion_time < current_customer_info[0]: # 이전 완료 시간보단 상담 고객의 시간이 더 큰 경우 
            previous_completion_time = current_customer_info[0] # 상담 시작 시간은 상담 고객의 내방 시간이 된다.

        # 해당 고객 상담 완료 처리
        answer.append(current_customer_info[1]) # 완료 고객명 담기
        previous_completion_time = addMinutes(previous_completion_time, 10) # 고객 상담 시작부터 10분 경과 시키기

    # 잔여 고객 처리
    if booked: # 잔여 예약 고객 순서대로 처리
        answer.extend([c[1] for c in booked])
    if unbooked: # 잔여 비예약 고객 순서대로 처리
        answer.extend([c[1] for c in unbooked])
    return answer


# 추가할 테스트 케이스 1 : 상담 완료 시간 이후 대기 중인 고객 없을 때 비예약 고객이 먼저 도착한 경우
# booked    : [["09:15", "hae"], ["10:05", "jee"]],
# unbooked  : [["09:04", "hee"], ["09:14", "eom"]],
# result    : ["hee", "eom", "hae", "jee"]

# 추가할 테스트 케이스 2 : 상담이 연속으로 있어서 이전 도착 손님과 10분 이상 차이가 나도 대기중인 고객(eg.20분)이 존재하는 경우
# booked    : [["00:02", "hae"], ["00:14", "jee"]],
# unbooked  : [["00:01", "hee"], ["00:03", "eom"]],
# result    : ["hee", "hae", "jee", "eom"]

# 유소연님 풀이
def solution(booked, unbooked):
    current_time = "00:00"
    result = []

    while booked and unbooked:
        if booked[0][0] > unbooked[0][0] and current_time < booked[0][0]:
            time, name = unbooked.pop(0)
        else:
            time, name = booked.pop(0)

        time = current_time if current_time > time else time 
        current_time = calculate_time(time)
        result.append(name)

    result.extend([b[1] for b in booked])
    result.extend([u[1] for u in unbooked])

    return result

def calculate_time(time):
    hour, minute = [int(x) for x in time.split(":")]
    minute += 10
    if minute >= 60:
        hour += 1
        minute -= 60
    # zfill : 남는 자릿수에 0채우기
    return str(hour).zfill(2) + ":" + str(minute).zfill(2)