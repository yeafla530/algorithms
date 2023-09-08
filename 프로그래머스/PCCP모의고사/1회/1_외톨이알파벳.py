# 2회 이상 나타난 알파벳이 2개이상의 부분으로 나뉘어있으면 외톨이 알파벳
from collections import defaultdict

def solution(input_string):
    answer = ''
    d = defaultdict()
    
    # hash저장
    for elem in input_string:
        if elem not in d:
            d[elem] = 0

    
    # 기준 문자 
    basic_string = input_string[0]
    # 전체 문자 돌기
    for i in range(1, len(input_string)):
        if basic_string != input_string[i]:            
            d[basic_string] += 1
            basic_string = input_string[i]
        
        if i == len(input_string)-1:
            d[input_string[i]] += 1

    
    for key in d.keys():
        if d[key] >= 2:
            answer += key

    
    if answer:        
        answer = list(answer)
        answer.sort()    

        answer = ''.join(answer)
    
    else:
        answer = 'N'
    
    return answer