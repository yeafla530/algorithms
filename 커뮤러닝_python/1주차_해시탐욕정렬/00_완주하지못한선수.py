def solution(participant, completion):
    # 참가자랑 완주자랑 하나하나 비교
    # 둘다 정렬
    participant.sort()
    completion.sort()
    # print(participant, completion)
    # 완주자 수만큼 loop
    for i in range(len(completion)):
        # 돌때까지 없는 참가자가 있으면
        if (participant[i] != completion[i]):
            # 해당 참가자 return
            return participant[i]
    # 끝까지 돌았는데 일치하지 않는 참가자가 없다면
    # 마지막 참가자 return
    return participant[-1]

