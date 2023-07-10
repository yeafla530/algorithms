// 제한 조건이 1,000,000
// O(N, Nlog)

// 큰 값이 나오면 이전 값 중 더 작은 값은 전부다 삭제한다
// 즉 스택의 바닥에서부터 탑은 큰수부터 작은수로 나열이 되어야함

const stack = []
function solution(number, k) {
    const stack = []
    let count = 0
    
    // number 한문자씩 비교 
    for (const item of number) {
        // 삭제 개수(count)가 k보다 적고
        // stack의 마지막 항이 지금 수보다 작으면 루프 돌리기
        while (count < k && stack[stack.length - 1] < item) {
            // 작으면 pop 후에, 지금의 item후에 push됨
            stack.pop()
            count += 1
        }
        // 돌릴 때마다 push됨
        stack.push(item)
    }
    // 위의 과정을 거쳤는데 count를 다 채우지 못한 경우
    // ex ) number : 9876543 k : 3
    // while (count < k) {
    //     // 맨끝의 항 pop
    //     stack.pop()
    //     count += 1
    // }
    // return stack.join("")
    
    // k개뺀 길이만큼만 join
    return stack.slice(0, number.length - k).join('');
    
    
}