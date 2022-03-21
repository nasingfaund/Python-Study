class TreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


tree = TreeNode(8)
tree.left = TreeNode(3)
tree.right = TreeNode(10)

tree.left.left = TreeNode(1)
tree.left.right = TreeNode(6)

tree.right.left = None
tree.right.right = TreeNode(14)

'''
         8
        /   \
       3     10
      / \      \
     1   6      14    
      
'''


def getTreeSum(node):
    pass


# рекурсивный обход в ширину
def recursiveBFS(node, left=None, right=None):

    if node:
        print(node.value)
    else:
        return

    if left:
        print(left.value)

    if right:
        print(right.value)

    if left:
        recursiveBFS(left, left, right)
    if right:
        recursiveBFS(right, left, right)


# рекурсивный обход в глубину
def recursiveDFS(node):
    if not node:
        return

    print(node.value)
    recursiveDFS(node.left)
    recursiveDFS(node.right)


recursiveBFS(tree)
