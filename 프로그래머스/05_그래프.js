// 무방향 그래프
// 방향 그래프

/////////////// 인접행렬
const graph = Array.from(
    Array(5),
    () => Array(5).fill(false)   
)


graph[0][1] = true
graph[0][3] = true
graph[1][2] = true
graph[2][0] = true
graph[2][4] = true
graph[3][2] = true
graph[4][0] = true

console.log(graph)

///////////// 인접리스트
const graph2 = Array.from(
    Array(5),
    () => []
);
graph2[0].push(1)
graph2[0].push(3)
graph2[1].push(2)
graph2[2].push(0)
graph2[2].push(4)
graph2[3].push(2)
graph2[4].push(0)

console.log(graph2)
