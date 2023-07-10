//////////// 힙
// 이진트리 형태를 가지며 우선순위가 높은 요소가 먼저 나가기 위해
// 요소가 삽입, 삭제 될 때 바로 정렬되는 특징이 있음


/////////// 우선순위 큐
// 우선순위가 높은 요소가 먼저 나가는 큐


////////// 힙의 특징
// 우선순위 높은 요소가 먼저 나간다
// 루트가 가장 큰 값이 되는 최대 힙과 루트가 가장 작은 값이 되는 최소힙이 있다
// 아쉽게 자바스크립트에선 직접구현해야됨

///////// 힙 요소 추가 알고리즘 
// 요소가 추가될때는 트리의가장 마지막에 정점에 위치
// 추가 후 부모 정점보다 우선순위가 높다면 부모 정점과 순서를 바꾼다
// 반복하면 결국 가장 우선순위가 높은 정점이 루트가 됨
// 완전 이진트리의높이는 logN이기에 힙의 요소 추가 알고리즘은 O(logN) 시간복잡도를 가짐

///////// 힙요소 제거
// 루트 정점만 제거가능
// 루트 정점이 제거된 후 가장 마지막 정점이 루트에 위치
// 루트 정점의 두 자식 정점중 더 우선순위가 높은 정점과 바꾼다
// 두 자식 정점이 우선순위가 더 낮을 때까지 반복한다
// 완전 이진트리의 높이는 logN이기에 힙의 요소 제거 알고리즘은 O(logN) 시간복잡도를 가진다


class MaxHeap {
    constructor() {
        this.heap = [null]
    }

    push(value) {
        this.heap.push(value)
        let currentIndex = this.heap.length - 1;
        let parentIndex = Math.floor(currentIndex / 2)

        while (parentIndex !== 0 && this.heap[parentIndex] < value) {
            const temp = this.heap[parentIndex];
            this.heap[parentIndex] = value;
            this.heap[currentIndex] = temp;

            currentIndex = parentIndex;
            parentIndex = Math.floor(currentIndex / 2);
        }
    }
    
    pop() {
        const returnValue = this.heap[1]
        this.heap[1] = this.heap.pop()

        let currentIndex = 1;
        let leftIndex = 2;
        let rightIndex = 3;
        while (
            this.heap[currentIndex] < this.heap[leftIndex] ||
            this.heap[currentIndex] < this.heap[rightIndex]
        ) {
            if (this.heap[leftIndex] < this.heap[rightIndex]) {
                const temp = this.heap[currentIndex];
                this.heap[currentIndex] = this.heap[rightIndex]
                this.heap[rightIndex] = temp;
                currentIndex = rightIndex
            } else {
                const temp = this.heap[currentIndex];
                this.heap[currentIndex] = this.heap[leftIndex]
                this.heap[leftIndex] = temp
                currentIndex = leftIndex
            }
            leftIndex = currentIndex * 2;
            rightIndex = currentIndex * 2 + 1
        }
        return returnValue
    }
}

const heap = new MaxHeap();
heap.push(45)
heap.push(36)
heap.push(54)
heap.push(27)
heap.push(63)
console.log(heap.heap)



const array = []
array.push(heap.pop())
array.push(heap.pop())
array.push(heap.pop())
array.push(heap.pop())
array.push(heap.pop())

console.log(array)