

class Node: 
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item

def inorder(root):

    if root:
        inorder(root.left)
        print(str(root.val) + "->", end='')
        inorder(root.right)


def postorder(root):

    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val) +  "->", end='')

def preorder(root):

    if root:
        print(str(root.val) + "->", end='')
        preorder(root.left)
        preorder(root.right)

root = Node(10)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left  = Node(6)
root.right.left = Node(7)
root.right.right = Node(8)

print("Inorder traversal ")
inorder(root)

print("\nPreorder traversal ")
preorder(root)

print("\nPostorder traversal ")
postorder(root)


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # Traverse preorder
    def traversePreOrder(self):
        print(self.val, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    # Traverse inorder
    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.val, end=' ')
        if self.right:
            self.right.traverseInOrder()

    # Traverse postorder
    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.val, end=' ')


root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)

print("\nPre order Traversal: ", end="")
root.traversePreOrder()
print("\nIn order Traversal: ", end="")
root.traverseInOrder()
print("\nPost order Traversal: ", end="")
root.traversePostOrder()


class Node:

    def __init__(self, item):
        self.item = item
        self.leftChild = None
        self.rightChild = None


def isFullTree(root):

    if root is None:
        return True

    if root.leftChild is None and root.rightChild is None:
        return True

    if root.leftChild is not None and root.rightChild is not None:
        return (isFullTree(root.leftChild) and isFullTree(root.rightChild))

    return False

root = Node(10)
root.rightChild = Node(2)
root.leftChild = Node(3)
root.leftChild.leftChild = Node(4)
root.leftChild.rightChild = Node(5)
root.rightChild.leftChild = Node(6)
root.rightChild.rightChild = Node(7)

if isFullTree(root):
    print("The tree is a full binary tree")
else:
    print("The tree is not a full binary tree")


class newNode:
    def __init__(self, k):
        self.key = k
        self.right = self.left = None

def calculateDepth(node):
    d = 0
    while (node is not None):
        d += 1
        node = node.left
    return d

def is_perfect(root, d, level=0):

    if (root is None):
        return True

    if (root.left is None and root.right is None):
        return (d == level +1)

    if (root.left is None or root.right is None):
        return False

    return (is_perfect(root.left, d, level +1) and
            is_perfect(root.right, d, level +1))

        


root = None
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)


print(is_perfect(root, calculateDepth(root)))






class testNode:
    def __init__(self, item):
        self.value = item
        self.right = None
        self.left = None


def is_even_tree(root):

    if root is None:
        return True

    if (root.left is None and root.right is None):
        return True

    if (root.left is None or root.right is None):
        return False

    return (is_even_tree(root.left) and is_even_tree(root.right))
    


    


root = testNode(1)
root.right = testNode(2)
root.left = testNode(3)
root.left.left = testNode(4)
root.left.right = testNode(5)
root.right.left = testNode(6)
root.right.right = testNode(7)

print(is_even_tree(root))


class Node:

    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


# Count the number of nodes
def count_nodes(root):
    if root is None:
        return 0
    return (1 + count_nodes(root.left) + count_nodes(root.right))


# Check if the tree is complete binary tree
def is_complete(root, index, numberNodes):

    # Check if the tree is empty
    if root is None:
        return True

    if index >= numberNodes:
        return False

    return (is_complete(root.left, 2 * index + 1, numberNodes)
            and is_complete(root.right, 2 * index + 2, numberNodes))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

node_count = count_nodes(root)
index = 0

if is_complete(root, index, node_count):
    print("The tree is a complete binary tree")
else:
    print("The tree is not a complete binary tree")


class Node:

    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Height:
    def __init__(self):
        self.height = 0


def isHeightBalanced(root, height):

    left_height = Height()
    right_height = Height()

    if root is None:
        return True

    l = isHeightBalanced(root.left, left_height)
    r = isHeightBalanced(root.right, right_height)
    

    height.height = max(left_height.height, right_height.height) +1

    print(left_height.height, right_height.height)
    
    if abs(left_height.height - right_height.height) <= 1:
        return l and r

    return False

height = Height()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.left.right = Node(7)
root.right.left = Node(8)
root.right.right = Node(9)

if isHeightBalanced(root, height):
    print('The tree is balanced')
else:
    print('The tree is not balanced')


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key) + "->", end='')
        inorder(root.right)

def insert(node, key):
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node

def minValueNode(node):
    current = node

    while(current.left is not None):
        current = current.left

    return current

def deleteNode(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif (key > root.key):
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)

    return root


root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 12)

print("Inorder traversal: ", end=' ')
inorder(root)

print("\nDelete 10")
root = deleteNode(root, 10)
print("Inorder traversal: ", end=' ')
inorder(root)

