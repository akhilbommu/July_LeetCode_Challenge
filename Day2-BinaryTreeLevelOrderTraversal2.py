from typing import List
from binarytree import Node


class BinaryTreeLevelOrderTraversal2:
    def __init__(self):
        self.res_list = []

    def preorder(self, node, level):
        if node is None:
            return
        while len(self.res_list) <= level:
            self.res_list.append([])

        self.preorder(node.left, level + 1)
        self.res_list[level].append(node.val)
        self.preorder(node.right, level + 1)

    def levelOrderBottom(self, root) -> List[List[int]]:
        self.preorder(root, 0)
        return self.res_list[::-1]


obj = BinaryTreeLevelOrderTraversal2()
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)
print(obj.levelOrderBottom(root))