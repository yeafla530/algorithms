def solution(a, b, c, d):
    answer = 0
    dic = {}
    arr = [a, b, c, d]
    for i in range(4):
        dic[arr[i]] = dic.get(arr[i], 0) + 1
    
    
    # 만약 1가지 숫자로 이루어져 있다면
    if len(dic) == 1:
        for k in dic.keys():
            return k * 1111
    
    lst = [[k, dic[k]] for k in dic.keys() ]
    print(lst)
    # 2가지 숫자로 이루어진 경우
    if len(dic) == 2:
        p, q = 0, 0
        is_three = False
        
        for [k, v] in lst:
            if v == 3:
                is_three = True
                p = k
            elif v == 1:
                q = k
            
            elif v == 2:
                if p == 0:
                    p = k
                else:
                    q = k
        # 2-1. 3개 같고, 1개 다름  
        if is_three:
            return (10 * p + q)**2
        
        # 2-2. 2개씩 같음
        else:
            return (p + q) * abs(p - q)
    
    elif len(dic) == 3:
        p, q, r = 0, 0, 0
        for [k, v] in lst:
            if v == 1:
                if q == 0:
                    q = k
                else:
                    r = k
        
        return q * r
    # 4가지 숫자
    elif len(dic) == 4:
        num = 987654321
        for [k, v] in lst:
            num = min(num, k)
        
        return num
