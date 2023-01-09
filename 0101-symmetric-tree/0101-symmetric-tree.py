# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def solver(left, right):
            # if one of the left or right is null other has to be null for symmetric
            if not left or not right:
                return left==right
            
            if left.val!=right.val:
                return False
            
            return solver(left.left , right.right) and solver(left.right, right.left)
    
        if not root: return False
        return solver(root.left, root.right)