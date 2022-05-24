from collections import deque


class TreeNode:
    left = right = None

    def __init__(self, value):
        self.value = value


root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)

root.left.left = TreeNode(1)
root.left.right = TreeNode(6)

root.right.left = None
root.right.right = TreeNode(14)

'''
         8
        /   \
       3     10
      / \      \
     1   6      14    
      
'''


# Итеративный обход в ширину с помощью очереди
# appendleft добавляет элемент В НАЧАЛО очереди
def getTreeSumWidth(root):
    sum = 0
    deque_ = deque()
    deque_.appendleft(root)

    while deque_:
        node = deque_.pop()
        sum += node.value

        if node.left:
            deque_.appendleft(node.left)

        if node.right:
            deque_.appendleft(node.right)

        print(node.value)

    return sum


# Итеративный обход в глубину с помощью стека
def getTreeSumDeep(root):

    sum = 0
    stack = [root]

    while stack:
        node = stack.pop()
        sum += node.value

        if node.left:
            stack.append(node.left)

        if node.right:
            stack.append(node.right)

        print(node.value)

    return sum


sum = 0


# рекурсивный обход в глубину
def rDFS(node):

    global sum

    if not node:
        return 0

    rDFS(node.left)
    rDFS(node.right)
    sum += node.value

    return sum


print(getTreeSumDeep(root))
