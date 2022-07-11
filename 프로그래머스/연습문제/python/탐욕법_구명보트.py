# 처음 풀이
# 효율성 테스트 통과 0
def solution(people, limit):
    # 한번에 최대 2명
    # 무게 제한
    # 구명보트 최대한 적게
    # 모든 사람을 구하기 위한 구명보트 개수 최솟값
    answer = 0
    i = 0
    min_w = 0
    # 정렬 후,,,
    people.sort(reverse=True)
    # print(people)
    while(len(people)):
        # i += 1 
        min_w = min(people)
        if (len(people) == 1):
            answer += 1
            return answer
        
        if (people[i] + min_w <= limit):
            people = people[i+1:-1]
            answer += 1
        else:
            people = people[i+1:]
            answer += 1
        # print(people)
    return answer