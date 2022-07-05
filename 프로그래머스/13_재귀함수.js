// 재귀함수랑 자기 자신을 호출하는 함수
// call stack에 쌓이기 때문에 스택 자료구조와 유사하게 동작
// 함수형 프로그래밍에선 루프 구현을 재귀로 구현하는 경우 많음
// 무한루프에 빠질 수있음

// JS에서 재귀함수
//// 콜스택에 제한이 있음
////// 자바스크립트 엔진마다 제한수는 다릅니다
////// 따라서 브라우저마다 다르지만 크롬의 경우 약 1만개이다
//// 꼬리 재귀가 제공되지 않음
//// 성능이 좋지 않음


// 재귀로 작성하면 쉽게 풀리는 코딩테스트문제가 있음

// 재귀로 구현해야 편한 알고리즘
//// 1. union-find
//// 2. DFS
//// 3. backtracking
// 불편함을 무시하면 더 빠른 성능으로 (JS에서) 작성할 수 있지만 코테는 빨리푸는것이 중요해서 추천하지 않음


// JS에서는 Call Stack에 제한이 있고 runtime error가 발생하고 프로그램이 종료될것임  
// 재귀 호출
function recursion(a) {
    // 탈출 코드가 없으면 무한 루프에 빠짐
    return recursion(a+1)
}

// 보통 if문을 통해 탈출
function recursion2(a) {
    if (a > 10) {
        // 무한 루프 방지를 위해
        // 탈출코드 작성
        return a
    }

    return recursion2(a + 1)
}

console.log(recursion2(5))

// 피보나치 수열
// 앞 두 항의 합이 뒤 항의 값이 되는 수열

// 1 1 2 3 5 8 13
function fibonacci(x) {
    if (x <= 2) {
        return 1
    }
    return fibonacci(x - 1) + fibonacci(x - 2)
}

console.log(fibonacci(7))


// 변수 없는 합병 정렬
// 합변 정렬

// 결합
const merge = (a, b) => {
    if (a.length === 0) return b;
    else if (b.length === 0) return a;
    else if (a[0] < b[0]) return [a[0], ...merge(a.slice(1), b)]
    else return [b[0], ...merge(a, b.slice(1))];
}

// 분해
const mergesort = (arr) => {
    if (arr.length < 2) return arr;
    else {
        const mid = Math.floor(arr.length / 2)
        return merge(mergesort(arr.slice(0, mid)), mergesort(arr.slice(mid)))
    }
}

console.log([10, 12, 13, 15, 20, 21, 22, 25]) 
console.log(mergesort([21, 10, 12, 20, 25, 13, 15, 22]))
