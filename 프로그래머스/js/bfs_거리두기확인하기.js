function canSit(place) {
    let room = place.map((x) => x.split(''))
    let queue = []
    // console.log(room)
    // 'P'자리 체크
    for (let i = 0; i < 5; i++) {
        for (let j = 0; j < 5; j++) {
            if (room[i][j] === 'P') {
                // console.log(i, j)
                queue.push([i, j])
            }
        }
    }
    // console.log(queue)
    
    let dx = [-1, 1, 0, 0];
    let dy = [0, 0, 1, -1];
    
    while (queue.length) {
        const [x, y] = queue.shift()
        
        for (let i = 0; i < 4; i++) {
            let nx = x + dx[i]
            let ny = y + dy[i]
            if (nx < 0 || nx >= 5 || ny < 0 || ny >= 5) continue
            if (room[nx][ny] === 'X') continue
            if (room[nx][ny] === 'P') return 0
            // console.log(nx, ny)
            
            for (let j = 0; j < 4; j++) {
                let menhatenX = nx + dx[j]
                let menhatenY = ny + dy[j]
                if (menhatenX < 0 || menhatenX >= 5 || menhatenY < 0 || menhatenY >= 5) continue
                
                if (menhatenX === x && menhatenY === y) continue
                if (room[menhatenX][menhatenY] === 'P') return 0
                
            }
            
        }
        
    }
    return 1
}
function solution(places) {
    var answer = [];
    for (const place of places) {
        answer.push(canSit(place))    
    }
    return answer;
}