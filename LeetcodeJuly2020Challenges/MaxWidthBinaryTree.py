# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # print(root)
        L = [root]
        lmax = len(L)
        while len(L) != 0:
            Ltemp = []
            flag = False
            for item in L:
                if item == None:
                    if flag:
                        Ltemp = Ltemp + [None, None]
                elif flag:
                    Ltemp = Ltemp + [item.left, item.right]
                else:
                    if item.left != None:
                        Ltemp = [item.left, item.right]
                        flag = True
                    elif item.right != None:
                        Ltemp = [item.right]
                        flag = True
            L = Ltemp
            # Pop off last Nones
            while len(L) != 0 and L[-1] == None:
                del L[-1]
            # Update lmax
            lmax = max(lmax, len(L))
        return lmax
