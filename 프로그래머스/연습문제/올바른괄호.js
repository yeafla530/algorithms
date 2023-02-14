function solution(s){
    let answer = true;
    let stack = []
    
    for (let i = 0; i < s.length; i++) {
        if (stack[stack.length - 1] === "(" && s[i] === ")")
        {
            stack.pop()    
        } else {
            stack.push(s[i])
        }
    }
    
    if (stack.length) {
        answer = false
    }
    

    return answer;
}



// 다른사람 풀이
function solution(s){
    let cum = 0

    for (let paren of s) {
        cum += paren === '(' ? 1 : -1
        if (cum < 0) {
            return false
        }
    }
    return cum === 0 ? true : false

}