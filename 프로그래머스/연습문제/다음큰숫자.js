function solution(n) {
    var answer = 0;
    let a = String(n.toString(2))
    a = a.split('')
    // 1의 개수
    let cnt1 = a.filter((n)=>n=='1').length
    
    // console.log(a, cnt1)
    
    for (let i = n+1; i < 1000000; i++) {
        let b = String(i.toString(2))
        b = b.split('')
        
        let cnt2 = b.filter((n)=>n=='1').length
        
        if (cnt1 == cnt2) {
            // console.log(b, cnt2)
            answer = i
            break
        }
    }
    
    return answer;
}