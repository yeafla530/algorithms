def solution(numbers):
    stack = []
    ans = [-1] * len(numbers)
    
    for i, value in enumerate(numbers):
        while stack and numbers[stack[-1]] < value:
            ans[stack.pop()] = value
                
        stack.append(i) # 현재 index값 담기
    
    
    return ans