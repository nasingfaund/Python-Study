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

# обход в ширину
def BFS(node):

    # случайно написал и сработало, но это больше напоминает обход в глубину
    # print(node.value)
    # if node.left:
    #     BFS(node.left)
    # if node.right:
    #     BFS(node.right)

    if node:
        print(node.value)
    BFS(node.left)
    BFS(node.right)


BFS(tree)