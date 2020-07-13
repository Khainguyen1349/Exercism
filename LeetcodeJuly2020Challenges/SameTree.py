import time
from TreeNode2 import TreeNode

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        ST = True
        Lp = [p]
        Lq = [q]
        if (Lp[0] == None) == (Lq[0] == None):
            while (len([i for i in Lp if i != None]) != 0) and ST:
                Lp_temp = []
                Lq_temp = []
                for i in range(len(Lp)):
                    if (Lp[i] == None) == (Lq[i] == None):
                        if Lp[i] != None:
                            if Lp[i].val != Lq[i].val:
                                ST = False
                            elif Lp[i].val == Lq[i].val:
                                Lp_temp = Lp_temp + [Lp[i].left, Lp[i].right] 
                                Lq_temp = Lq_temp + [Lq[i].left, Lq[i].right] 
                    else:
                        ST = False
                Lp = Lp_temp
                Lq = Lq_temp
        else:
            ST = False
        return ST

null = None
input1 = [3,9,20,null,null,null,7]

tree1 = TreeNode()
tree1.readTreeList(input1)
tree1.printTreeNode()

input2 = [3,9,20,null,null,null,8]

tree2 = TreeNode()
tree2.readTreeList(input2)
tree2.printTreeNode()

start = time.time()
if Solution().isSameTree(tree1,tree2):
    print('Same trees!')
else:
    print('Not same trees!')

end = time.time()
print(end - start)
        
