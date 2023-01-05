# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def solver(root,maxi):
            
            if not root: return 0
            
            left=max(0, solver(root.left,maxi))
            right=max(0, solver(root.right, maxi))
            
            # max with 0 used to handel negative values
                
            maxi[0]=max(maxi[0], left+right+root.val)
            
            return root.val+ max(left, right)
        
        maxi=[float('-inf')]
        solver(root,maxi)
        return maxi[0]