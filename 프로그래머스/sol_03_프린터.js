class Node {
    constructor(value) {
        this.value = value
        this.next = null
    }
}

class Queue {
    constructor() {
        this.head = null
        this.tail = null
    }
    
    enqueue(value) {
        const newNode = new Node(value)
        if (this.head === null) {
            this.head = this.tail = newNode
        } else {
            this.tail.next = newNode
            this.tail = newNode
        }
    }
    
    dequeue() {
        const value = this.head.value
        this.head = this.head.next
        return value
    }
    
    peek() {
        return this.head.value
    }
}

// 가장 앞에 있는 문서(J)를 대기목록에서 꺼냄
// J보다 중요도 높은 문서 한개라도 존재하면 J를 대기 목록의 가장 마지막에 넣음
// 그렇지 않으면 J인쇄
function solution(priorities, location) {
    // var answer = 0;
    let q = new Queue()
    for (let i = 0; i < priorities.length; i++) {
        // 우선순위와 index
        q.enqueue([priorities[i], i])
    }
    
    // 우선순위별로
    priorities.sort((a, b) => b - a)
    // q가 빌때까지
    
    // 몇번째 프린트 되는지
    let count = 0
    while (true) {
    
        const currentValue = q.peek()
        console.log(currentValue)
        // 입력된 순서대로의 우선순위 < 정렬한 우선순위
        if (currentValue[0] < priorities[count]) {
            // currentValue의 우선순위보다 높은 우선순위가 있으니 대기목록 마지막에 넣기
            q.enqueue(q.dequeue())
        // 입력된 순서대로 우선순위 >= 정렬한 우선순위
        } else {
            // 그렇지 않으면 인쇄
            
            // 현재 위치 === 원하는 위치
            let value = q.dequeue()
            count += 1
            if (value[1] === location) {
                return count   
            }
        }
        
    }
    return count
}