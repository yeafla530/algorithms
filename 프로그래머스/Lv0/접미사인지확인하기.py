def solution(my_string, is_suffix):
    answer = 0
    # print(my_string[-len(is_suffix):len(my_string)])
    if my_string[-len(is_suffix):] == is_suffix:
        return 1
    
    else:
        return 0
    
