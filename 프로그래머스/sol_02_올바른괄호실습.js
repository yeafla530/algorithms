function solution(s){
    // 왜 시간초과..?
    // let stack = []
    let count = 0
    
    for (const st of s) {
        if (st === '(') {
            // stack.push(st)
            count += 1
            
        } else {
            // stack이 비어있는데 ')'인 경우
            // if (stack.length === 0) {
            if (count === 0) {
                return false
            } 
            // stack.pop()
            count -= 1
        }
    }

    // return stack.length === 0
    return count === 0

}


///// 나의 풀이
function solution(s){
    let answer = false
    const stack = []
    let sArray = s.split("");
    for (let i = 0; i < sArray.length; i++) {
        if(sArray[0] === ")"){
            return false
            break
        }
        if (sArray[i] === "(") {
            stack.push("(")
        } else {
            stack.pop()

        }
    }
    return stack.length === 0

}