// 내 풀이
function solution(id_list, report, k) {
    // 한번에 한명 유저 신고 가능
    // 동일한 유저에 대한 신고는 1번만 가능
    // k번 이상 신고된 유저는 게시판 이용이 정지됨 => 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송
    // 마지막에 한꺼번에 게시판 이용 정지시켜 정지 메일 발송
    let answer = [];
    let countDict = {}
    let reported = new Object
    // console.log(report)
    
    for (let i = 0 ; i < id_list.length; i++) {
        countDict[id_list[i]] = 0
    }
    // console.log(countDict)
    
    for (const word of report) {
        let name = word.split(' ')
        
        if (reported[name[1]] && reported[name[1]].includes(name[0])) {
            continue
        } else {
            reported[name[1]] ? reported[name[1]].push(name[0]) : reported[name[1]] = [name[0]]   
        }
    }
    
    for (const [key, val] of Object.entries(reported)) {
        if (val.length >= k) {
            // console.log('확인')
            for (let item of val) {
                countDict[item] += 1
            }
        }
    }
    
    answer = Object.values(countDict)

            
    
    // console.log(answer)
    return answer;
}

// 다른 사람 풀이
// set과 map을 이용한 풀이
function solution(id_list, report, k) {
    // 중복 제거 & 나누기
    let reports = [...new Set(report)].map(a=>{return a.split(' ')});
    let counts = new Map();
    // 신고 받은 사람 수 세기 
    // Map : set, get 이용하기
    for (const bad of reports){
        counts.set(bad[1],counts.get(bad[1])+1||1)
    }
    let good = new Map();
    for(const report of reports){
        // k번 이상 신고 받은 사람 있으면
        if(counts.get(report[1])>=k){
            // 
            good.set(report[0],good.get(report[0])+1||1)
        }
    }
    let answer = id_list.map(a=>good.get(a)||0)
    return answer;
}