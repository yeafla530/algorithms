//////////// 내 풀이
function solution(numbers) {
    var answer = 0;
    for (let i = 0; i < 10; i++) {
        if (numbers.includes(i)) {
            continue
        } else {
            answer += i 
        }
    }
    return answer;
}

//////////// 남의 풀이
function solution(numbers) {
    return 45 - numbers.reduce((acc, cur) => acc + cur, 0)
}