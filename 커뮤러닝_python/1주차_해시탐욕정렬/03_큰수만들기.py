def solution(number, k):
    answer = ''
    count = 0
    stack = []
    lst = list(map(int, number))
    # print(lst)

   
    
    for i in range(len(number)):
        # k값 넘기면 break
        # print(stack)
        if (k == count):
            stack.append(number[i:])
            # print(count)
            break
        # 아닌 경우
        else:
            # stack에 들어있는 값들이 지금 값보다 크거나 같을때까지 pop()
            while(len(stack) != 0 and stack[-1] < number[i] and count != k):
                stack.pop()
                count += 1
            
            # 그리고 stack에 넣는다
            stack.append(number[i])

    
    # 987654321 의 경우
    if (count != k):
        stack = stack[:len(stack)-(k-count)]


    return "".join(stack) 



# 다른사람 풀이
def solution(number, k):
    answer = [] # Stack

    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
    
    return ''.join(answer[:len(answer) - k])