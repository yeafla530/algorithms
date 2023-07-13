# runtime error - 재귀

ans = 0
def solution(numbers):
    answer = ''
    arr = []
    
    def find_max_num():
        string_num = ''
        
        for i in arr:
            string_num += str(numbers[i])
    
        return string_num
    
    def check(n):
        global ans
        if n == len(numbers):
            num = find_max_num()
            ans = max(ans, int(num))
            return
        
        
        for i in range(len(numbers)):
            if i not in arr:
                arr.append(i)
                check(n+1)
                arr.pop()
    
    
    check(0)
    
    
    return str(ans)


### 원리를 이해해야한다
def solution(numbers):
    numbers = list(map(str, numbers))    
    # numbers의 원소값이 1000이하이므로 반복되는수가 최소 3자리 이상이도록 만들어준 뒤 정렬
    # ex) 3, 30 => 333, 303030 => 333이 string으로 정렬시 더 큼 
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    
    # 숫자값을 string으로 변경해야하므로 int처리해주기
    return str(int("".join(numbers)))