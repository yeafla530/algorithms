# 동시에 카페에 머무는 사람들
# 같은 종류 음료 항상 같은 시간
# 음료 목록을 이용해 손님들 동시에 최대 몇명 머물렀는지 알기

from collections import deque

def solution(menu, order, k):
    queue = deque()
    busy = -1
    idx = answer = 0
    
    for t in range(k * (len(order)-1) + 1):
        # 0초외 사람들이 올때 대기에 넣어줌
        if k * idx == t:
            queue.append(order[idx])
            idx += 1
        # 음료를 1잔 만들었을 때
        if busy == t:
            # 1명이 빠진다
            queue.popleft()
            # 다시 제조해야함
            busy= -1
        
        # 음료를 만들기 시작, 대기하는 사람이 있을 때
        if busy == -1 and len(queue) > 0:
            # 음료만드는데 걸리는 시간
            busy = t + menu[queue[0]]
        
        answer = max(answer, len(queue))
    
    return answer