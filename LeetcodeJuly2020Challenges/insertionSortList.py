import time
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def makeListNode(li):
    if len(li) > 0:
        LN = ListNode(li[0], None)
        LNtemp = LN
        for i in li[1:]:
            LNNexttemp = ListNode(i)
            LNtemp.next = LNNexttemp
            LNtemp = LNNexttemp
        return LN
    else:
        return None

def printListNode(LN):
    LNtemp = LN
    while LNtemp != None:
        print(LNtemp.val)
        LNtemp = LNtemp.next


start = time.time()

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        l = []
        while head != None:
            l.append(head.val)
            head = head.next
        print(l)
        if len(l) > 0:
            l.sort()
            return makeListNode(l)
        else: 
            return None
    
inputs = [4,2,1,3]

LN = makeListNode(inputs)
printListNode(LN)

h = Solution()
print(printListNode(h.insertionSortList(LN)))

end = time.time()
print(end - start)
        
