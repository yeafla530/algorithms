// 퀸을 둔 행은 가지치기
// 퀸을 둔 열은 가지치기
// 퀸을 둔 대각선 왼, 오는 가지치기

function check(queen, row) {
    // 자금까지 행 체크
    for (let i = 0; i < row; i += 1) {
        if (queen[row] === queen[i] || Math.abs(queen[row] - queen[i]) === row - i) {
            return false
        }
    }
    return true
}

function search(queen, row) {
    let n = queen.length;
    let count = 0
    // row는 1씩 증가시킬것임
    if (n === row) { // 행 끝까지 가면 return (재귀 종료)
        return 1
    }
    
    for (let col = 0; col < n; col++) { // 열 
        queen[row] = col
        if (check(queen, row)) {
            count += search(queen, row+1)
        }
    }
    
    return count
    
}


function solution(n) {
    var answer = 0;
    // index = 행
    // value = 열
    // 대각선 = index의 차이 == value의 차이
    let queen = Array(n).fill(0)
    return search(queen, 0);
}