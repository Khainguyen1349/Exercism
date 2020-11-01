# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        l = head
        value = 0
        while l != None:
            value = value*2 + l.val
            l = l.next
        return value
