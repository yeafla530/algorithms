def solution(registered_list, new_id):
    answer = ''
    # 아이디 추천
    # 포함되어있다면
        # S, N으로 분리
        # 문자열 N을 10진수 숫자로 변환한 값을 n
        # N이 비어있으면 n = 0
        # n에 1을 더한 값 n+1을 문자열로 변환한 값을 N1
        # new_id 변경후 다시 1로 돌아감 
    
    d = {}
    for i in registered_list:
        if not d.get(i, 0):
            d[i] = d.get(i, 0) + 1
    
    while new_id in d:
        n = ''
        s = ''
        for i in range(len(new_id)):
            if new_id[i].isdigit():
                n += new_id[i]
            else:
                s += new_id[i]

        if len(n):
            n = int(n) + 1
        else:
            n = 1
        
        new_id = s + str(n)

    answer = new_id
    return answer
                

    return answer

solution(["AABCA.QA", "AABC..QX", "BBBC.Y..", ".A...T.A", "....EE..", ".M.XXEXQ", "KL.TBBBQ"])