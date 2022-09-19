function rotate(orders) {
    let n = orders.length
    let count = 0
    temp =  Array.from(Array(n), () => Array(n).fill(0))
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            temp[i][j] = orders[n-1-j][i]
        }
    }

    return temp
}

function solution(orders) {
    var answer = [];
    // 학생수
    let n = orders.length

    
    // 90도 회전
    orders = rotate(orders)
    let halfStudent = Math.round(n / 2)
    // console.log(halfStudent)


    console.log(orders[0])
    while (true) {
        // 점수 초기화
        let score = new Array(n).fill(0)
        // 남은 투표수
        let len = orders.length
        // 종료조건인지 확인
        let isEnd = false

        // 투표수 세기
        for (let x = 0; x < n; x++) {
            score[x] = orders[0].filter(elem => elem === x).length
        }
        let minNum = 987654321
        for (let i = 0; i < n; i++) {
            if (score[i] && minNum > score[i]) {
                minNum = score[i]
            }
        }
        console.log('score', score) // [0, 0, 2, 2]


        
        // 가장 적게 받은 학생들
        let minCount = []
        

        for (let x = 0; x < n; x++) {
            // 반수 이상이면 출석번호가 큰 사람 break
            console.log('반수이상?', score[n-x-1], halfStudent)
            if (score[n-x-1] >= halfStudent) {
                classMonitor = n-x-1
                isEnd = true

                answer.push(n-len+1)
                answer.push(classMonitor)
                break
            // 반수 안넘었으면
            } else {
                // 가장 적게 득표한 후보 담기
                // console.log("Math.min(score)", Math.min(...score))
                
                if (minNum == score[x]) {
                    minCount.push(x)
                }
            }
        }

        
        console.log('o', orders)

        if (isEnd) {
            break
        }

        let minStudent = 0
        // console.log(minCount)
        // 가장 적게 득표한 후보
        minStudent = minCount[0]
        // console.log(minStudent)
        
        orders.splice(0, 1)
        // 탈락시키기
        for (let i = 0; i < len-1; i++) {
           console.log(orders[i])
           orders[i].splice(minStudent, 1)
        }
            
        
    }
    
    return answer;
}

solution(
    [[2, 3, 4, 0, 1], [1, 4, 3, 2, 0], [4, 1, 0, 2, 3], [3, 2, 1, 4, 0], [0, 3, 2, 1, 4]]
)