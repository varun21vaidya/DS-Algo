# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
# #       we know that inorder traversal for tree will always have sorted sequence
# #       so we can validate a tree based on this, if any tree doesnt have increasing sequence
# #       we will return False
# #       so first traverse inorder and save it in array
# #       and using linear scan check if it is increasing, if not return False, if loop ends return True
#         def inorder(root,output):
#             if root:
#                 inorder(root.left,output)
#                 output.append(root.val)
#                 inorder(root.right,output)
                
#         res=[]
#         inorder(root,res)
#         for i in range(len(res)-1):
#             if res[i]>=res[i+1]:
#                 return False
            
#         return True
    

#     WITHOUT EXTRA SPACE 
        def validate(root,minimum, maximum):
            if not root: return True
            if not minimum < root.val< maximum: return False
            
            return validate(root.left, minimum,root.val) and validate(root.right,root.val,maximum)
        
        return validate(root,float('-inf'),float('inf'))
        
            