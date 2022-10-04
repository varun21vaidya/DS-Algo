# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
#         def solver(root):
#             if not root: return 0
#             if root:
#                 left= solver(root.left)
#                 right= solver(root.right)
                
#                 return max(left,right)+1

            
        def solver(root,d):
            if not root: return d
            return max(solver(root.left,d+1),solver(root.right,d+1))
        return solver(root,0)