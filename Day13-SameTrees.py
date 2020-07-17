from binarytree import Node


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SameTree:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True

        if (p is not None and q is not None) and (p.val == q.val):
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return False


obj = SameTree()
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)

print(obj.isSameTree(root1, root2))

root3 = Node(1)
root3.left = Node(2)

root4 = Node(1)
root4.right = Node(2)

print(obj.isSameTree(root3, root4))