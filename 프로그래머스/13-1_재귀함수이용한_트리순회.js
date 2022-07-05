//      1
//      / \
//     /   \
//    2     \
//   / \     3
//  4   5   / \
//         6   \
//              7
//             / \
//            8   9

// 전위 순회
// 노드 방문 후 왼쪽 서브 트리를 전위순회한 다음 오른쪽 서브트리를 전위순회함
// 1, 2, 4, 5, 3, 6, 7, 8, 9

// preorder(tree) {
//     방문(tree.root);
//     preorder(tree.left);
//     preorder(tree.right);
// }




// 중위순회
// 왼쪽 서브트리를 중위순회 한 후 노드 방문한 다음 
// 4, 2, 5, 1, 6, 3, 8, 7, 9
// inorder(tree) {
//     inorder(tree.left);
//     방문(tree.root);
//     inorder(tree.right);
// }

// 후위 순회
// 왼쪽 서브트리 후위순회 후 오른쪽 서브트리 후위순회한 다음 노드 방문
// 4, 5, 2, 6, 8, 9, 7, 3, 1
// postorder(tree) {
//     postorder(tree.left);
//     postorder(tree.right);
//     방문(tree.root);
// }


class Node {
    constructor(value) {
        this.value = value
        this.left = null
        this.right = null
    }
}

class Tree {
    constructor(node) {
        this.root = node;
    }

    preorder(currentNode) { // 전위순회
        console.log(currentNode.value);
        if (currentNode.left) this.preorder(currentNode.left)
        if (currentNode.right) this.preorder(currentNode.right);
    }

    inorder(currentNode) { // 중위순회
        if (currentNode.left) this.inorder(currentNode.left)
        console.log(currentNode.value);
        if (currentNode.right) this.inorder(currentNode.right)
    }

    postorder(currentNode) { // 후위순회
        if (currentNode.left) this.postorder(currentNode.left)
        if (currentNode.right) this.postorder(currentNode.right)
        console.log(currentNode.value)

    }
}

//       9
//      / \
//     /   \
//    3     \
//   / \     8
//  2   5   /  
//       \ 7   
//        4       

const tree = new Tree(new Node(9))
tree.root.left = new Node(3)
tree.root.right = new Node(8)
tree.root.left.left = new Node(2)
tree.root.left.right = new Node(5)
tree.root.right.right = new Node(7)
tree.root.left.right.right = new Node(4)

tree.preorder(tree.root)
// tree.inorder(tree.root)
// tree.postorder(tree.root)

