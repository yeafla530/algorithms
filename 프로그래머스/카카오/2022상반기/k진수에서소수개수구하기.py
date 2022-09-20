
def solution(n, k):
    answer = -1
    # n => k진수 변환
    # 조건에 맞는 소수 찾기
    # 1. 0P0 => 소수 양쪽에 0이 있는 경우
    # 2. P0 => 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우
    # 3. 0P => 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우
    # 4. P => 소수 양쪽에 아무것도 없는 경우
    # P는 자릿수에 0을 포함하지 않는 소수
    arr = []
    
    # 1. k진수 변환 
    while n:
        r = n % k
        # print(r)
        n = n // k
        # print(n)
        arr.append(r)
    arr = arr[::-1]
        
    
    # 2. 소수 판별 (P 찾기)
    str_p = ""
    p = 0
    p_list = []
    for i in range(len(arr)):
        if arr[i] == 0:
            str_p = ""
            continue
        str_p += str(arr[i])
        p = int(str_p)
        if p == 0:
            continue
        
        a = int(p**0.5)
        is_decimal = True
        
        if p <= 1:
            continue
        
        
        for j in range(2, a):
            if not p % j:
                is_decimal = False
                break
        
        if is_decimal:
            s = i - len(str_p) + 1
            e = i
            length = len(arr)
            is_possible = False
            # print(s, e, arr[s:e+1], arr[s-1] if s - 1 >= 0 else "False", arr[e+1] if e + 1 < length else "False")
            # 조건 확인
            if s - 1 >= 0 and e + 1< length:
                if arr[s-1] == 0 and arr[e+1] == 0:
                    is_possible = True
            
            elif s == 0 and e + 1 < length:
                if arr[e+1] == 0:
                    is_possible = True
                    
            elif e == length-1 and s - 1 >= 0:
                if arr[s-1] == 0:
                    is_possible = True
                    
            elif s == 0 and e == length-1: 
                is_possible = True
                
                
        if is_possible:
            p_list.append(p)
        
        if i+1 != len(arr) and arr[i+1] == 0:
            str_p = ""
        
    # print(p_list)
    answer = len(p_list)
    return answer