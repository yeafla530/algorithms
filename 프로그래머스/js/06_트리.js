// 루트 정점 제외한 모든 정점은 반드시 하나의 부모 정점을 가진다
// 정점이 N개인 트리는 반드시 N-1개의 간선을 가진다
// 루트에서 특정 정점으로 가는 경로는 유일하다

/////////// 이진트리
// 1. 정점이 N개인 이진트리는 최악의 경우 높이가 N이될수있다
// 2. 정점이 N개인 포화 또는 완전 이진트리 높이는 logN이다
// 3. 높이가 h인 포화 이진트리는 2^h - 1개의 정점을 가진다
// 4. 일반적인 이진트리 사용하는 경우 많지 않음 (예시)
    // 이진탐색트리
    // 힙
    // AVL 트리
    // 레드블래트리


// 이진트리 구현방법
// 배열 혹은 요소에 링크가 2개 존재하는 연결리스트로 구현가능

////////// Array
// 0번 인덱스는 비워둔다
// Left = Index * 2
// Right = Index * 2 + 1
// Parent = floor(Index / 2)
const tree1 = [
    undefined,
    // 1
    9,
    // 1*2, 1*2+1
    3, 8,
    // 2*2, 2*2+1, 3*2, 3*2+1
    2, 5, undefined, 7,
    // 4*2, 4*2+1, 5*2, 5*2+1
    undefined, undefined, undefined, 4
]

///////////// 이진트리
class Node {
    constructor(value) {
        this.value = value
        this.left = null
        this.right = null
    }
}
class Queue {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    enqueue(newValue) {
        const newNode = new Node(newValue)
        if (this.head === null) {
            this.head = this.tail = newNode;
        } else {
            this.tail.next = newNode;
            this.tail = newNode;
        }
    }

    dequeue() {
        const value = this.head.value
        this.head = this.head.next;
        return value
    }

    peek() {
        return this.head.value;
    }
}

class Tree {
    constructor(node) {
        this.root = node 
    }

    display() {
        const queue = new Queue()
        queue.enqueueu(this.root);
        while (queue.size) {
            const currentNode = queue.dequeue()
            console.log(currentNode.value)
            if (currentNode.left) queue.enqueue(currentNode.left)
            if (currentNode.right) queue.enqueue(currentNode.right)
        }
    }


}

const tree = new Tree(new Node(9))
tree.root.left = new Node(3)
tree.root.right = new Node(8)
tree.root.left.left = new Node(2)
tree.root.left.right = new Node(5)
tree.root.right.right = new Node(7)
tree.root.left.right.right = new Node(4)

console.log(tree)