def invertTree(node):
    # рекурсивный способ

    #         if not node:
    #             return None

    #         node.right, node.left = node.left, node.right
    #         self.invertTree(node.left)
    #         self.invertTree(node.right)

    # итеративный способ

    # stack = [node]
    #
    # while stack:
    #
    #     node_ = stack.pop()
    #
    #     if not node_:
    #         continue
    #
    #     node_.right, node_.left = node_.left, node_.right
    #     stack.append(node_.left)
    #     stack.append(node_.right)

    return node
