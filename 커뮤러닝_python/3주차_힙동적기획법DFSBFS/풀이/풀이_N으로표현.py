def solution(N, number):
    # 중복 허용하지 않고 계산된 수를 품
    s = [set() for _ in range(8)]

    for i, x in enumerate(s, start=1):
        # 5, 55, 555, 5555...
        x.add(int(str(N) * i))
    
    for i in range(1, 8):
        # 0-0, 0-1, 0-2, 0-3 ,,, 
        # 3번의 연산 : 1&2, 2&1, 3&0
        for j in range(i):
            # 집합에 있는 수
            # 앞선 수 : ex ) s[0]: 한개 연산, s[1]: 2개 연산, s[2]: 3개 연산까지
            for op1 in s[j]:
                # 뒤의 수 : ex ) s[2]: 3개 연산, s[1]: 2개 연산, s[0]: 1개 연산
                # 앞선 수 뒤의 수의 연산을 통해 총 4개를 이용한 연산들을 알 수 있음
                for op2 in s[i-j-1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
        
        if number in s[i]:
            answer = i + 1
            break
    else:
        answer = -1


    return asnwer

solution(5, 11)