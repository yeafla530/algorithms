def solution(id_list, report, k):
    answer = [0]*len(id_list)
    # 각 유저는 한번에 한명의 유저 신고
    # 한 유저 여러번 신고할수도 있지만 동일한 유저에 대한 신고는 1회로 처리됨
    # k번 이상 신고된 유저는 게시판 이용이 정지됨
    # 해당 유저 신고한 모든 유저에게 정지사실을 메일로 보냄
    # 유저가 신고한 모든 내용 취합해 마지막에 한번에 게시판 이용정지 시키면서 정지메일 발송
    
    # 개수세기
    d = {}
    ids = [[] for _ in range(len(report))]
    
    for i in range(len(report)):
        r, reported = report[i].split()
        
        
        idx = id_list.index(reported)
        # print(idx)
        if r not in ids[idx]:
            d[reported] = d.get(reported, 0) + 1
            ids[idx].append(r)
        
    for key, value in d.items():
        # k번이상 신고당한 사람
        if value >= k:
            # i = 신고당한 사람의 index
            i = id_list.index(key)
            # 신고한 사람들 리스트 뽑기
            # print(ids)
            for p in ids[i]:
                # 신고한 사람의 index찾기
                index = id_list.index(p)
                answer[index] += 1
    return answer