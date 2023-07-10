// 연결리스트는 각 요소를 포인터로 연결하여 관리하는 선형 자료구조
// 단일연결리스트, 더블연결리스트, 환원연결리스트

// 추가 삭제시 시간효율높음

// 핵심 : 찾기O(n), 추가O(1), 삭제O(1)

/////// 단일 연결리스트
class Node {
    constructor(value) {
        this.value = value;
        this.next = null
    }
}

class SinglyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    append(newValue) {
        const newNode = new Node(newValue)
        // 첫번째로 들어왔을 떄
        if (this.head === null) {
            this.head = newNode
            this.tail = newNode
        } else {
            this.tail.next = newNode
            this.tail = newNode
        }
    }
    find(value) {
        let currNode = this.head;
        while (currentNode.value !== value) {
            currNode = currNode.next // 그 다음 데이터를 갖고있음
        }
    }
}
