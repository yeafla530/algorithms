def solution(number, limit, power):
    answer = 0
    def getNum(n):
        cnt = 0
        
        for i in range(1, int(n**(1/2))+1):
            if n % i == 0:
                cnt += 1
                
                if i*i < n:
                    cnt += 1
        
        return cnt
        
    for i in range(1, number+1):
        result = getNum(i)
        
        if (result <= limit):
            answer += result
        else:
            answer += power
    
    
    
    return answer