class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        newHead = None
        while head:
            next_node = head.next
            head.next = newHead
            newHead = head
            head = next_node
        return newHead
