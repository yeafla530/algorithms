def solution(record):
    answer = []
    # 채팅방을 나간 후, 새로운 닉네임으로 다시 들어간다.
    # 채팅방에서 닉네임을 변경한다.
    nickname = {}
    store = []
    for r in record:
        arr = r.split()
        
        if arr[0] == "Enter":
            store.append([arr[1], 'enter'])
            nickname[arr[1]] = arr[2]
                
        elif arr[0] == "Leave":
            store.append([arr[1], 'leave'])
            
        else:
            nickname[arr[1]] = arr[2]
    
    for s in store:
        if s[1] == 'enter':
            answer.append(f"{nickname[s[0]]}님이 들어왔습니다.")
        else:
            answer.append(f"{nickname[s[0]]}님이 나갔습니다.")
            
    
    return answer