class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def readList(List):
    ListOfNodes = []
    for i in range(len(List)):       
        ListOfNodes.append(ListNode(List[i],None))
    for i in range(len(List)-1):
        ListOfNodes[i].next = ListOfNodes[i+1]
    return ListOfNodes[0]
a = [1,2,3]
