# 내 풀이
from collections import deque

def solution(priorities, location):
    count = 0
    queue = deque([])
    for i in range(0, len(priorities)):
        queue.append([i, priorities[i]])

    while True:
        prt = queue.popleft()
        if (len([x[0] for x in queue if x[1] > prt[1]])):
            # print('print안함')
            queue.append(prt)
        else:
            # print('print함')
            count += 1 
            if (prt[0] == location):
                return count

    # print(queue)
    return count