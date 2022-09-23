# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]):
        self.d1=defaultdict(list)
        def check(root,val,level):
            if not root:
                return
            self.d1[val].append((root.val,level))
            if root.left:
                check(root.left,val-1,level+1)
            if root.right:
                check(root.right,val+1,level+1)
        check(root,0,0)
        l=[]
        #print(self.d1)
        for x in sorted(self.d1.keys()):
            l1=self.d1[x]
            l1.sort(key=lambda x:(x[1],x[0]))
            l2=[]
            for x in l1:
                l2.append(x[0])
            l.append(l2)
        return l