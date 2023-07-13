def solution(score):
    answer = [0] * len(score)
    arr = []
    
    for i in range(len(score)):
        arr.append((i, score[i][0] + score[i][1]))
        
    arr.sort(key=lambda x: -x[1])
    print(arr)
    
    degree = 0
    same_score = 0
    before_score = 987654321
    idx = 0
    
    while idx < len(score):
        num, avg = arr[idx]
        
        if before_score == avg:
            same_score += 1
            
        else:
            before_score = avg
            degree += 1 + same_score
            same_score = 0
                
        answer[num] = degree
        idx += 1
    
    return answer


### 다른 사람 풀이
def solution(score):
    score_sum = sorted([sum(i) for i in score], reverse=True)
    
    d = {}
    
    for i, n in enumerate(score_sum):
        if n not in d:
            d[n] = i + 1
        
    for i in score:
        print(d[sum(i)])
    return [d[sum(i)] for i in score]