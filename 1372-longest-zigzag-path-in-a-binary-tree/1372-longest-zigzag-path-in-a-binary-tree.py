# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root,direction,count):
            if not root:
                return count
            if direction=="left":
                dfs(root.left,"right",count+1)
                dfs(root.right,"left",1)
                
            else:
                dfs(root.right, "left",count+1)
                dfs(root.left,"right",1)
                
            counted[0]=max(count,counted[0])
        
        counted=[0]
        dfs(root,"left",0)
        dfs(root,"right",0)
        return counted[0]