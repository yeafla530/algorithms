answer = []
    
def get_gene(pose):
    global answer
    
    n, p = pose
    
    if n == 1:
        return 'Rr'
    
    mother_gene = get_gene((n-1, (p-1)//4+1))
    
    case = ('RR', 'Rr', 'Rr', 'rr')
    
    if mother_gene == 'Rr': return case[p%4-1]
    else: return mother_gene
    

def solution(queries):
    global answer
    
    for i in range(len(queries)):
        ans = get_gene(queries[i])
        answer.append(ans)
    
    return answer