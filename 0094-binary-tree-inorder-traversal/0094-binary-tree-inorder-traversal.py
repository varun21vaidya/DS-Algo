# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         def helper(root):
#             if root:
#                 helper(root.left)
#                 res.append(root.val)
#                 helper(root.right)
#         res=[]
#         helper(root)
#         return res
    
        # while there is current node, go to extreme left
        # and append to stack each node
        # now you will reach null ie curr becomes null
        # now else, get element from top of stack, addd it to result and move to right
        # now again it checks if something is to right
        # at some point stack will become empty, break the loop
        
        curr=root
        stack=[]
        res=[]
        while True:
            if curr:
                stack.append(curr)
                curr=curr.left
            else:
                if not stack: return res
                curr=stack.pop()
                res.append(curr.val)
                curr=curr.right
                
        return res
                
                
        

        
            
        