// 내풀이 
// 11번부터 시간초과
function solution(gems) {
    var select = []; // 선택한 보석
    let gemObject = new Set(gems) // 보석 종류
    let minCount = 987654321 // 구간 개수
    let store = [] // 가장짧은 구간 저장 [start, end] 
    
    let start = 0 // 시작점
    let end = 0 // 끝점 + 1 (slice)
    let objLength = [...gemObject].length
    while (true) {
        end += 1
        
        // end가 끝에 도달하면 start바꿔줌
        if (end > gems.length) {
            start += 1
            end = start + 1
        }
        // 보석 종류 개수보다 작을 경우
        if (gems.length-start < objLength) {
            break
        }
        
    
        
        select = gems.slice(start, end)
        
        if ([...new Set(select)].length === objLength) {
            if (minCount >= end-start) {
                minCount = end-start
                store.push([minCount, start, end])
                
                start += 1
                end = start + 1
                continue
                // console.log(store)
            }
        }
    }
    // 개수순으로 정렬
    store.sort((a, b) => a[0] - b[0])
    // start내림차순으로 정렬
    let newStore = []
    for (let item of store) {
        if (item[0] === minCount) {
            item.splice(1, 1, item[1]+1)
            newStore.push(item.slice(1, 3))
        }
    }
    newStore.sort((a, b) => b[0] - a[0])
    // console.log(newStore)
    
    return newStore.pop()
    
   
}

// 실패의 원인 
// 풀이를 보니 모든 보석을 구매할 수 있으면 end는 그자리에 고정, 선택한 보석 개수가 최소가 될 때까지 start만 +1씩 증가시킴
// 나는 start +1 하면 end = start + 1로 같이 변경해줬음 



function solution(gems) {
    let answer = [0, gems.length] // 가장 긴 길이로 초기화
    let start = 0;
    let end = 0;

    const gemKinds = new Set(gems).size // 겹치지 않는 보석 수
    const collect = new Map(); // 보석들을 담아둘 변수 (key, value), get, set사용
    collect.set(gems[0], 1) // 시작하면서 첫 보석을 먼저 담는다

    // 두 포인터가 끝에 도닥하면 종료
    while (start < gems.length && end < gems.length) {
        if (collect.size === gemKinds) { // 모든 보석을 구매할 수 있다면
            if (end - start < answer[1] - answer[0]) { // 구간을 갱신
                answer = [start + 1, end + 1]
            }
            // start 증가시키기 전에 현재 start의 보석 개수 줄이기
            collect.set(gems[start], collect.get(gems[start]) - 1)
            // 0이 되면 해당 원소 삭제
            // 개수가 같으면 다음 턴에 모든 보석을 구매할 수 있다고 인식하기 때문에
            if (collect.get(gems[start] === 0)) {
                collect.delete(gems[start])
            }
            // start 개수 증가시키기
            start += 1

            console.log(collect)
        } else { // 모든 보석을 구매할 수 없다면
            end += 1 // 두번째 포인터 증가
            // 보석개수 증가시킴
            // 이런식으로 출력됨
            // Map { 'DIA' => 3, 'EMERALD' => 1, 'SAPPHIRE' => 1, 'RUBY' => 1 }
            // 보석이 있으면 기존 개수에서 1 추가하고, 없으면 1
            collect.set(gems[end], 1 + (collect.get(gems[end]) || 0))

        }
    }
}