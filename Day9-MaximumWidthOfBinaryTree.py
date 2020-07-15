# Definition for a binary tree node.
from binarytree import Node


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaximumWidthOfBinaryTree:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0

        max_width = 1
        queue = [[root, 0]]
        while len(queue) > 0:
            count = len(queue)
            start, end = queue[0][1], queue[-1][1]
            max_width = max(max_width, end - start + 1)

            for i in range(count):
                temp = queue[0]
                index = temp[1] - start
                queue.pop(0)
                if temp[0].left is not None:
                    queue.append([temp[0].left, 2 * index + 1])
                if temp[0].right is not None:
                    queue.append([temp[0].right, 2 * (index + 1)])
        return max_width


obj = MaximumWidthOfBinaryTree()
root = Node(1)
root.left = Node(3)
root.right = Node(2)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.right = Node(9)
print(obj.widthOfBinaryTree(root))


