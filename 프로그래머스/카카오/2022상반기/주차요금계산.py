import math
def solution(fees, records):
    answer = []
    
    # 입차
    intime = {}
    # 누적시간
    result = {}
    
    for record in records:
        time, car, status = record.split(' ')
        h, m = time.split(":")
        c_time = int(h) * 60 + int(m)
        # 입차한다면
        if status == "IN":
            intime[car] = intime.get(car, 0) + c_time
            
        # 출차한다면
        else:
            prefix_time = c_time - intime[car]
            result[car] = result.get(car, 0) + prefix_time
            del(intime[car])
            
    
    if len(intime):
        c_time = 23*60 + 59
        for x in intime.keys():
            prefix_time = c_time - intime[x]
            result[x] = result.get(x, 0) + prefix_time

    arr = list(result.keys())
    arr.sort()
    
    for x in arr:
        # 기본시간 이하라면
        if result[x] <= fees[0]:
            fee = fees[1]
            
        else:
            fee = fees[1] + math.ceil((result[x] - fees[0]) / fees[2]) * fees[3]
        answer.append(fee)
    
    
    return answer




###### 풀이
###### TIP : for문 돌면서 dict 올림은 sorted를 사용하면된다
import math
def convert_time(time):
    h, m = time.split(":")
    return int(h) * 60 + int(m)

def solution(fees, records):
    answer = []
    
    # 입차
    intime = {}
    # 누적시간
    result = {}
    
    for record in records:
        time, car, status = record.split(' ')
        c_time = convert_time(time)
        
        # 입차한다면
        if status == "IN":
            intime[car] = intime.get(car, 0) + c_time
            
        # 출차한다면
        else:
            prefix_time = c_time - intime[car]
            result[car] = result.get(car, 0) + prefix_time
            del intime[car]
            
    
        
    for k, v in intime.items():
        prefix_time = 23*60+59 - v
        result[k] = result.get(k, 0) + prefix_time


    
    for k, v in sorted(result.items()):
        # 기본시간 이하라면
        if v <= fees[0]:
            answer.append(fees[1])
            
        else:
            answer.append(fees[1] + math.ceil((v - fees[0]) / fees[2]) * fees[3])
    
    
    return answer