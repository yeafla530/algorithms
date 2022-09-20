import math
def solution(fees, records):
    answer = []
    # 입차된 후에 출차된 내역이 없다면, 23:59에 출차된 것으로 간주합니다.
    # 누적 주차 시간이 기본 시간이하라면, 기본 요금을 청구합니다.
    # 기본 시간을 초과하면, 기본 요금에 더해서, 초과한 시간에 대해서 단위 시간 마다 단위 요금을 청구
        # 초과한 시간이 단위 시간으로 나누어 떨어지지 않으면, 올림합니다.
    # records의 원소들은 시각을 기준으로 오름차순으로 정렬되어 주어집니다.
    
    # fees : 기본시간, 기본요금, 추가시간, 추가요금
    d = {}
    cur_time = 0
    
    for record in records:        
        time, car_num, status = record.split(' ')
        h, m = time.split(":")
        # print(int(h), int(m))
        # 현재 시간
        cur_time = 60 * int(h) + int(m)
        
        # IN
        if status == "IN":
            # 처음 입차하는 경우
            if car_num not in d:
                d[car_num] = [cur_time, "IN"]
            # 이미 입차한경우
            else:
                d[car_num][0] += cur_time
                d[car_num][1] = "IN"
        
        # OUT
        else:
            d[car_num] = [d[car_num][0]-cur_time, "OUT"]
            
    
    keys = list(d.keys())
    keys.sort()
    print(d)
    # 만약 출차 안한경우
    for x in keys:
        if d[x][1] == "IN":
            time = 23*60 + 59
            all_time = math.ceil(abs(d[x][0] - time))
            # 기본 시간
            
        else:
            all_time = math.ceil(abs(d[x][0]))
        # print(all_time)
        
        
        if all_time <= fees[0]:
            fee = fees[1]
            
        else:
            remain = (all_time-fees[0]) % fees[2]
            if remain:
                time = all_time - fees[0] - remain + fees[2]
            else:
                time = all_time - fees[0]
            
            # print(time, all_time)
            fee = fees[1] + (time // fees[2]) * fees[3]
            # print(fee)
        
        answer.append(fee)
            
    
    
    return answer