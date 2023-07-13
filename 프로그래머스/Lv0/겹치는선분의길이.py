def solution(lines):
    answer = 0
    nums = {}
    for i in range(3):
        x1, x2 = lines[i]
        x1 += 100
        x2 += 100
        
        for n in range(x1+1, x2+1):
            if n not in nums:
                nums[n] = nums.get(n, 0)
            
            elif nums[n] == 0:
                nums[n] = 1
    
    print(nums)
    for n in nums:
        if nums[n] == 1:
            answer += 1
    return answer