## 내 풀이
def solution(today, terms, privacies):
    answer = []
    # 오늘 날(today)보다 기간이 작은 경우
    td_list = today.split('.')
    td = int(td_list[0]) * 12 * 28 + int(td_list[1]) * 28 + int(td_list[2])
    
    day_dic = {}
    # terms => dict
    for i in range(len(terms)):
        l = terms[i].split(' ')
        day_dic[l[0]] = day_dic.get(l[0], 0)
        day_dic[l[0]] = int(l[1]) * 28
    
    for (idx, str) in enumerate(privacies, 1):
        new_day = 0
        
        day, term = str.split(" ")
        day_lst = day.split('.')
        new_day = int(day_lst[0]) * 12 * 28 + int(day_lst[1]) * 28 + int(day_lst[2])
        new_day += day_dic[term]
    
        if td >= new_day:
            answer.append(idx)
            
    return answer


#### 다른사람 풀이
def to_days(date):
    year, month, day = map(int, date.split('.'))
    return year * 28 * 12 + month * 28 + day

def solution(today, terms, privacies):
    months = {v[0]: int(v[2:]) * 28 for v in terms}
    today = to_days(today)
    
    expire = [
        i + 1 for i, privacy in enumerate(privacies)
        if to_days(privacy[:-2]) + months[privacy[-1]] <= today
    ]
    
    return expire