"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        linked = []
        item = head
        while (item != None) or (len(linked) != 0):
            if item == None:
                item = linked[-1]
                prev_item.next = item
                item.prev = prev_item
                del linked[-1]
            else:
                if item.child != None:
                    if item.next != None:
                        linked.append(item.next)
                    item.next = item.child
                    item.child.prev = item
                    item.child = None
                prev_item = item
                item = item.next
        return head
