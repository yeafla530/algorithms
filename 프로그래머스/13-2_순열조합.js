// 직접 구현해야함
// 재귀 이용하면 쉽게 만들 수 있음
// 성능이나 콜스택 위험으로 스택으로 구현하는 것이 좋지만
// 순열과 조합 자체가 시간복잡도가 굉장히 크기 때문에 코딩테스트에서 n이 크게 나오는 경우 많지 않음
// 외워라

// 순열 O(n!)
// 중복 허용, 위치만 바꿔서도 다른걸로 취급
function permutations(arr, n) {
    // 1개만 뽑는다면 그대로 순열은 반환한다. 탈출 조건으로도 사용된다
    if (n === 1) return arr.map((v) => [v])
    
    let result = [];
    
    // 요소 순환
    arr.forEach((fixed, idx, arr) => {
        // 현재 index를 제외한 요소를 추출한다.
        // index번째는 선택된 요소
        const rest = arr.filter((_, index) => index !== idx);
        console.log('rest', rest)
        // 선택된 요소를 제외하고 재귀 호출한다.
        const perms = permutations(rest, n - 1)
        console.log("perms", perms)
        // 선택된 요소와 재귀 호출을 통해 구한 순열을 합쳐줌
        const combine = perms.map((v) => [fixed, ...v])
        console.log("combine", combine)
        // 결과값을 추가한다
        result.push(...combine)
    })

    // 결과 반환
    return result
}

console.log(permutations([1, 3, 5, 7], 3))

// 조합 O(2^n)
// 중복 허용x 
function combinations(arr, n) {
    // 1개만 뽑는다면 그대로 조합 반환
    // 탈출조건으로 사용
    if (n === 1) return arr.map((v) => [v]);
    const result = []

    // 요소 순환
    arr.forEach((fixed, idx, arr) => {
        // 현재 index 이후 요소 추출
        // index번째는 선택된 요소
        const rest = arr.slice(idx + 1); // idx+1이후 원소들
        // 선택된 요소 이전 요소들 제외하고 재귀 호출
        const combis = combinations(rest, n-1);
        // 선택된 요소와 재귀 호출을 통해 구한 조합을 합쳐준다.
        const combine = combis.map((v) => [fixed, ...v])
        // 결과값을 추가한다
        result.push(...combine)
    })
    // 결과 반환
    return result
}

console.log(combinations([1, 3, 5, 7], 2))
