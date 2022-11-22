def solution(number, limit, power):
    answer = 0
    arr = [0] * (number+1)
    
    for n in range(1, number+1):
        for i in range(1, n+1):
            if arr[n] == limit and n % i == 0:
                arr[n] = power
                break
            
            if n % i == 0:
                arr[n] += 1
        
    
    answer = sum(arr)
            
            
    
    
    
    print(arr)
    answer = sum(arr)
    return answer