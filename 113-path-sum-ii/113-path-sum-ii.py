# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def dfs(root,temp,summ):
            if not root: return
            summ+=root.val
            temp.append(root.val)

            if not root.left and not root.right:
                if summ==targetSum:
                    ans.append(temp.copy())
            else:
                dfs(root.left,temp,summ)
                dfs(root.right,temp,summ)
                
            temp.pop()
            
        ans=[]
        dfs(root,[],0)
        return ans
            
            