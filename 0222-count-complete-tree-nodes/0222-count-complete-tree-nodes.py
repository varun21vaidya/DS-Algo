# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        lst=[]
        def helper(root):
            if root:
                helper(root.left)
                lst.append(root.val)
                helper(root.right)
         
        helper(root)
        return len(lst)