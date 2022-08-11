# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self,root, minn, maxx):
        if root==None: return True
        if (minn!=None and minn.val>=root.val): return False
        if (maxx!=None and maxx.val<=root.val): return False
        
        return self.helper(root.left, minn, root) and self.helper(root.right, root, maxx)
    
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, None, None)
    
