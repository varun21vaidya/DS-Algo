# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(root,res):
            if not root:return
            res[0]+=1
            dfs(root.left,res)
            dfs(root.right,res)
        
        if not root:return 0
        res=[0]
        dfs(root,res)
        return res[0]