# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        
        # Recursive
        
#         if not root: return False

#         if not root.left and not root.right and root.val==targetSum:
#             return True

#         if root:
#             return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)
        
#         # Iterative
#         if not root: return False
#         stack=[(root,root.val)]
#         while stack:
#             root,val=stack.pop()
#             if not root.left and not root.right and val==targetSum:
#                 return True
#             if root.left:
#                 stack.append((root.left, val+root.left.val))
#             if root.right:
#                 stack.append((root.right, val+root.right.val))
#         return False
    
    
        if not root: return False
        stack=[(root,targetSum)]
        while stack:
            root,Sum=stack.pop()
            if not root.left and not root.right and root.val==Sum:
                return True
            if root.left:
                stack.append((root.left, Sum-root.val))
            if root.right:
                stack.append((root.right, Sum-root.val))
        return False
                
        