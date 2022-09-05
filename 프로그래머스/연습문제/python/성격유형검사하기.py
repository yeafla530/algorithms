def solution(survey, choices):
    answer = ''

    mbti = {'R':0, 'T': 0, 'C': 0, 'F':0, 'J':0, 'M': 0, 'A':0, 'N':0}
    arr = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    
    for i in range(len(survey)):
        if choices[i] < 4:
            mbti[survey[i][0]] += 4- choices[i]
        else:
            mbti[survey[i][1]] += choices[i] - 4
    print(mbti)
    answer = ''
    
    for a in arr:
        if mbti[a[0]] > mbti[a[1]]:
            answer += a[0]
        elif mbti[a[0]] < mbti[a[1]]:
            answer += a[1]
        else:
            answer += sorted(a)[0]
            
            
    
    return answer


# 다른 사람 풀이
def solution(survey, choices):

    my_dict = {"RT":0,"CF":0,"JM":0,"AN":0}
    for A,B in zip(survey,choices):
        if A not in my_dict.keys():
            A = A[::-1]
            my_dict[A] -= B-4
        else:
            my_dict[A] += B-4

    result = ""
    for name in my_dict.keys():
        if my_dict[name] > 0:
            result += name[1]
        elif my_dict[name] < 0:
            result += name[0]
        else:
            result += sorted(name)[0]

    return result