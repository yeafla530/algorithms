def solution(k):
    answer = 0
    d = {0:6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
    a = {}
    def check(number,cnt, k):
        if cnt >= k:
            if cnt == k:
                if number not in a:
                    a[number] = a.get(number, 0) + 1
                
            return
            
        for key, v in d.items():
            if number != '' or k <= 6:
                check(number+str(key), cnt+v, k)
            else:
                if key > 0:
                    check(number+str(key), cnt+v, k)




    check('', 0, k)
    answer = len(a)


    return answer