#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while (head != None) and (head.val == val):
            head  = head.next
        currentNode = head
        if (head != None):
            cont = True
            while cont:
                while (currentNode.next != None) and (currentNode.next.val == val):
                    currentNode.next = currentNode.next.next
                currentNode = currentNode.next
                if currentNode == None:
                    cont = False
        return head
