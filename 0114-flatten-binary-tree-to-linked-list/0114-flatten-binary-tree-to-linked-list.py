# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def solver(root):
            if not root: return
            
            left=solver(root.left)
            right=solver(root.right)
            
            if left:
                root.right=left
                while left and left.right:
                    left=left.right
                left.right=right
                root.left=None
                
            return root
        main=root 
        solver(root)