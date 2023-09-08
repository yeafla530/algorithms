import heapq
# 프로그램이 종료되는 시각과, 프로그램의 정수마다 대기시간의 합


def solution(program):
    answer = [0] * 11
    heap = []
    
    program.sort(key=lambda x: (x[1], x[0])) # 우선순위, 시간 기준으로 정렬
    
    time = 0
    
    while program or heap:
        while program and program[0][1] <= time:
            heapq.heappush(heap, program.pop(0))
        
        print(heap)
        if program and not heap:
            time = program[0][1]
        
            heapq.heappush(heap, program.pop(0))
        
        temp = heapq.heappop(heap)

        answer[temp[0]] += (time - temp[1])
        time += temp[2]
    
    answer[0] = time
    return answer