# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
#         def preorder(root):
#             if root:
#                 ans.append(root.val)
#                 preorder(root.left)
#                 preorder(root.right)
        
#         ans=[]
#         preorder(root)
#         return ans
    
    
        ans=[]
        if not root: return ans
        stack=[root]
        while stack:
            temp=stack.pop()
            ans.append(temp.val)
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
                
        return ans
        
                
    
        