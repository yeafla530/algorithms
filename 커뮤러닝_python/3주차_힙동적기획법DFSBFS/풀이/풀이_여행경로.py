# 사전을 이용해 각 공항에서 출발하는 항공권의 집합(리스트)을 표현
# 알파벳 역순으로 정렬
def solution(tickets):
    routes = {}
    for t in tickets:
        # get : t[0]이 None이면 []를 초기값으로 
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    
    for r in routes:
        routes[r].sort(reverse = True)

    stack = ["ICN"]
    # 가려는 경로
    path = []

    while len(stack) > 0:
        top = stack[-1]
        # 갈수있는 공항이 없으면
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]
    
    return path[::-1]