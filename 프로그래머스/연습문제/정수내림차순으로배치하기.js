function solution(n) {
    var answer = 0;
    n = String(n).split('')
    // console.log(n)
    answer = n.sort((a, b) => b - a).join('')
    // console.log(answer1)
    return +answer;
}