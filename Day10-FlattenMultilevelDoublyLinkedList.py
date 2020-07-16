# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class FlattenMultilevelDoublyLinkedList:
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        current = head
        while current is not None:
            if current.child is None:
                current = current.next
            else:
                next_ = current.next
                child_ = current.child

                current.next = child_
                child_.prev = current
                current.child = None

                while child_.next is not None:
                    child_ = child_.next
                child_.next = next_

                if next_ is not None:
                    next_.prev = child_
        return head


