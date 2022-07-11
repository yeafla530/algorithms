# hash사용
def solution(participant, completion):
    dict = {}
    for x in participant:
        # get : value값 얻기
        # get(x, 디폴트값)
        dict[x] = dict.get(x, 0) + 1
    
    for y in completion:
        dict[y] = dict.get(y) - 1
    # print(dict)
    # 나의 풀이
    for d in dict:
        if (dict.get(d)):
            return d

    # 강사님 표현
    dnf = [k for (k, v) in dict.items() if v > 0]
    answer = dnf[0]
    return 

## 이전 풀이
# 정렬 사용
# 테스트는 통과하지만,,
# NloN의 시간복잡도를 가짐
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


}