def solution(arr, query):
    answer = []
    
    for i in range(len(query)):
        n = query[i]

        # 짝수
        if i % 2 == 0:
            arr = arr[:n+1]
        # 홀수
        else:
            arr = arr[n:]
            
            
    return arr