// 최단 거리 구할때 bfs사용
function solution(maps) {
    var answer = 0;
    // 방향 설정 : 아래 오 왼 위
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    
    // 행열 
    row = maps.length
    column = maps[0].length
    
    // 방향 담을 queue 
    queue = []
    queue.push([0, 0])
    
    // 초기 graph
    graph = Array.from(Array(row), () => Array(column).fill(-1))
    graph[0][0] = 1
    
    while (queue.length) {
        let [y, x] = queue.shift()
        for (let i = 0; i < 4; i++) {
            // 방향 변경한 값
            nx = x + dx[i]
            ny = y + dy[i]
            
            // 미로를 벗어나지 않고
            if (nx >= 0 && nx < column && ny >= 0 && ny < row) {
                // 길이 있으면
                if (maps[ny][nx] === 1 && graph[ny][nx] === -1) {
                    // 그 전 경로 step + 1
                    graph[ny][nx] = graph[y][x] + 1
                    queue.push([ny, nx])
                }
            }
        }
    }
    
    // 맨 마지막 값이 정답
    answer = graph[row-1][column-1]
    
    
    return answer;
}