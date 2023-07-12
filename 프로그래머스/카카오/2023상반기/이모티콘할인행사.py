def solution(users, emoticons):
    answer = []
    
    percent = []
    sort_arr = []
    # 조건?
    def search(cnt):
        if cnt == len(emoticons):
            result = [0] * 2
            # users들 정보             
            for idx, [per, max_money] in enumerate(users):
                # discount percent 담은 arr
                total_money = 0
                for i in range(len(emoticons)):
                    # 각 사람마다 구매하는 금액 arr
                    if per <= percent[i]:
                        total_money += int(int(emoticons[i]) * (100 - percent[i]) * 0.01)
                
                # print(percent, total_money, max_money)
                # 이모티콘 다 더했는데 user가 정한 가격보다 높다면 가입
                if max_money <= total_money:
                    result[0] += 1   
                # 아니면 구매
                else:
                    result[1] += total_money
                    
            sort_arr.append(result)                    

                        
            
            
            
            return
        
        
        for discount in range(10, 50, 10):
            percent.append(discount)
            search(cnt+1)
            percent.pop()
        
    search(0)
    sort_arr.sort(key=lambda x: (-x[0], -x[1]))
    
    
    
    return sort_arr[0]


