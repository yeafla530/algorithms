// BFS
// 탐색 시작 노드를 큐에 삽입하고 방문처리
// 큐에서 노드를 꺼내 해당 노드의 인접노드 중 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
// 2번과정 더이상 수행할수 없을 때까지 반복
const bfs = function(graph, v, visited) {
    let queue = []
    visited[v] = true
    queue.push(v)
    while (!(queue.length === 0)) {
        v = queue.shift()
        console.log(v) // 1 2 3 8 7 4 5 6
        for (const a of graph[v]) {
            if (visited[a] !== true) {
                visited[a] = true
                queue.push(a)
            }
        }
    }

}


let graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6 ,8],
    [1, 7]
]

let visited = Array(9).fill(false)
bfs(graph, 1, visited)



///// dfs
// 탐색시작 노드를 스택에 삽입하고 방문처리
// 스택 최상단 노드에 방문하지 않은 인접노드 있으면 그 인접노드를 스택에 넣고 방문처리
// 방문하지 않은 인접노드가 없으면 스택에서 최상단 노드를 꺼낸다
// 2번의 과정을 더이상 수행할 수 없을때까지 반복
function dfs(graph, v, visited) {
    visited[v] = true
    console.log(v + '\t')
    for (const i of graph[v]) {
        if (!visited[i]) {
            dfs(graph, i, visited)
        }
    }
}

let graph2 = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6 ,8],
    [1, 7]
]

let visited2 = Array(9).fill(false)
dfs(graph, 1, visited2)