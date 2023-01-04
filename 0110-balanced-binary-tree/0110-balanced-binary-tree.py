# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def solver(root):
            
            if not root:
                return 0

            left=solver(root.left)
            if left==-1: return -1
            
            right=solver(root.right)

            if right==-1 or abs(left-right)>1:
                return -1

            return max(left,right)+1
            
            
        if not root: return True
        
        return solver(root)!=-1