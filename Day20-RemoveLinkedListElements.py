# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class RemoveLinkedListElements:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head is not None and head.val == val:
            head = head.next
        current = head
        while current is not None:
            if current.next is not None and current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return head


