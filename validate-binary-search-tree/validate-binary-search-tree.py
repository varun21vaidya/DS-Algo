# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(root,output):
            if root:
                inorder(root.left,output)
                output.append(root.val)
                inorder(root.right,output)
                
        res=[]
        inorder(root,res)
        for i in range(len(res)-1):
            if res[i]>=res[i+1]:
                return False
            
        return True
            