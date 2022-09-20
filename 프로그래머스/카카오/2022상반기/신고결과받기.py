def solution(id_list, report, k):
    answer = [0]*len(id_list)
    # 신고한 user
    report_user = {}
    # 신고당한 user
    result_user = {}
    
    for x in report:
        r, reported = x.split(' ')
        if r not in report_user:
            report_user[r] = set()
            report_user[r].add(reported)
        else:
            # print(report_user[r])
            report_user[r].add(reported)
            
        
        if reported not in result_user:
            result_user[reported] = set()
            result_user[reported].add(r)
        else:
            result_user[reported].add(r)
    
    # print(result_user, report_user)
    for i, x in enumerate(id_list):
        # 메일을 몇개 받았는지 출력
        # 신고한 이력이 있으면
        if x in report_user:
            # 신고받은 사람의 신고횟수 세기
            for y in report_user[x]:
                if len(result_user[y]) >= k:
                    answer[i] += 1
                
            
    
    # print(answer)
    
    return answer