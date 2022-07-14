function solution(s) {
    var answer = [];
    s = s.split('')
    let stack = [] // string to list
    let str = '' // 들어갈 문자
    let start = 0 // 괄호 시작, 끝
    let count = 0 // 괄호 index
    
    // 하나하나 loop
    for (let i = 1; i < s.length - 1; i++) {
        // '{' 시작되면
        if (s[i] === '{') {
            // 시작을 알림
            start = 1
            stack.push([])
            continue
        }
        
        // '}'되면 
        if (s[i] === '}') {
            stack[count].push(Number(str))
            str = ''
            // 끝을 알림
            start = 0
            // idx 추가
            count += 1
            continue
        }
        
        // 괄호가 끝나지 않았으면 
        if (start === 1) {
            // '.'나오면 push
            if (s[i] === ',') {
                stack[count].push(Number(str))
                str = ''
            // 아니면 문자열 +
            } else {
                str += s[i]
            }

        // 괄호가 끝나고 시작될때까지 액션x
        } else {
            continue
        }
    }
    
    // 길이순 정렬
    stack.sort((a, b) => a.length - b.length)
    
    // 1개짜리부터 들어있으면 pass시키는 방식
    for (const item of stack) {
        for (let x of item) {
            // console.log(x)
            if (!(answer.includes(x))) {
                answer.push(x)
            } else {
                continue
            }
        }
    }
    
    // console.log(stack)
    return answer;
}


// 다른 사람 풀이 응용
function solution(s) {
    var answer = [];
    //////////// 응용한 부분
    s = s.replace("{{", "").replace("}}", "").split("},{") // [ '20,111', '111' ]
    s = s.map(a => a.split(',')) // [ [ '20', '111' ], [ '111' ] ]
    s.sort((a, b) => a.length - b.length)
    /////////////
    
    for (const item of s) {
        for (let x of item) {
            // console.log(x)
            if (!(answer.includes(parseInt(x)))) {
                answer.push(parseInt(x))
            } else {
                continue
            }
        }
    }
    
    // console.log(stack)
    return answer;
}