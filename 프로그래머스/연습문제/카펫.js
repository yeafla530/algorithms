// 완전탐색
function solution(brown, yellow) {
    var answer = [];
    // 가로보다 세로가 더 짧거나 같음
    // 제곱근 이하로 나눴을 때 가로 세로 길이 구분
    for (let i = 1; i*i <= yellow; i++) {
        // 안나눠지면 +1 해서 다시
        if (yellow % i) {
            continue
        } else {
            let height = i
            let width = yellow / height
            // 갈색 세로 블럭 개수 => 옆에 height개수 채우기 (2번)
            let brown_y = height * 2
            // 갈색 가로 블럭 개수 => 가로로 추가된 갈색(2개) + 노란색 블럭 개수 (2번)
            let brown_x = (width + 2) * 2
            
            // 개수가 같아지면 return
            if (brown_y + brown_x === brown) {
                answer.push(width + 2)
                answer.push(height + 2)
                return answer
            } 
            
        }
    }
}