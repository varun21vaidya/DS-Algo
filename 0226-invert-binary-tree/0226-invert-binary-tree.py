# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def solver(root):
            if  root:
                temp=root.left
                root.left=root.right
                root.right=temp
                solver(root.left)
                solver(root.right)
            
            
    
        solver(root)
        return root