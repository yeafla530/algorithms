def solution(num, total):
    answer = []
    mid = total // num
    
    if num % 2:
        answer.append(mid)
        for _ in range(num//2):
            answer.append(min(answer)-1)
            answer.append(max(answer)+1)
    else:
        mid2 = mid+1
        answer.append(mid)
        answer.append(mid2)
        for _ in range((num-2)//2):
            answer.append(min(answer)-1)
            answer.append(max(answer)+1)
        
    answer.sort()
    return answer