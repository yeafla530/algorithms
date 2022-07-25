def solution(tickets):
    ticket = dict()
    tickets.sort(reverse = True)

    # dict로 출발지 - 도찾기 list정의
    for start, end in tickets:
        if start in ticket:
            ticket[start].append(end)
        else:
            ticket[start] = [end]
    print(ticket)

    route = ["ICN"]
    answer = []

    while route:
        st = route[-1]
        # print(st)
        if st not in ticket or len(ticket[st]) == 0:
            answer.append(route.pop())
        else:
            route.append(ticket[st].pop())
        
    answer.reverse()



    return answer