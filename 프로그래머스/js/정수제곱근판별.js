function solution(n) {
    var answer = 0;
    let ch = Math.sqrt(n)
    console.log(ch)
    if (Number.isInteger(ch)) {
        return (ch + 1)**2
    } 
    return -1 
    // return answer;
}