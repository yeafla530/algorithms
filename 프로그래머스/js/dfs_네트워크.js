function dfs(computers, n, i, visited) {
    visited[i] = 1
    for (let j = 0; j < n; j++) {
        if (i !== j && computers[i][j] === 1) {
            if (!visited[j]) {
                dfs(computers, n, j, visited)
            }
        }
    }
}

function solution(n, computers) {
    let answer = 0
    let visited = Array(n).fill(0)
    for (let i = 0; i < n; i++) {
        if (visited[i] === 0) {
            dfs(computers, n, i, visited)
            answer += 1
        }
    }
    
    
    return answer;
}
