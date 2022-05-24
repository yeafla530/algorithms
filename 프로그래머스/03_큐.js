class Node {
    constructor(value) {
        this.value = value
        this.next = null
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

const q = new Queue()
q.enqueue(2)
console.log(q)
q.enqueue(5)
console.log(q)
q.enqueue(7)
console.log(q)
console.log(q.dequeue())
console.log(q.dequeue())
console.log(q)

