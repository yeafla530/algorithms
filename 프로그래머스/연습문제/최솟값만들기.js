function solution(A,B){
    var answer = 0;
    A.sort((a, b) => a - b)
    B.sort((a, b) => b - a)
    
    for (let i = 0; i < A.length; i++) {
        answer += A[i] * B[i]
    }
    

    return answer;
}

// reduce
function solution(A,B){
    var answer = 0;
    A.sort((a, b) => a - b)
    B.sort((a, b) => b - a)
    
    answer = A.reduce((total, cur, idx) => total + cur * B[idx], 0)
      
    
    

    return answer;
}