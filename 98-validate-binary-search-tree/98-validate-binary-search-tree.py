# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
# Inorder traversals can be useful because we know that the inorder traversal of a BST
# results in traversing the tree in an essentially increasing, sorted fashion. 
# So essentially, the helper method is just performing this inorder traversal. 
# so through each iteration, we keep updating the minn and maxx to contain root. 
# But if we see that root is less than the root.left or root is greater than root.right
# then we just break and return false
    
    def helper(self,root, minn, maxx):
        if root==None: return True
        if (minn!=None and minn.val>=root.val): return False
        if (maxx!=None and maxx.val<=root.val): return False
        
        return self.helper(root.left, minn, root) and self.helper(root.right, root, maxx)
    
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, None, None)
    
