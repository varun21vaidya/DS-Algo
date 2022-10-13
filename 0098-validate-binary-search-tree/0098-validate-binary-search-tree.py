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

#     we will check if root.val>root.left.val and root.val<root.right.val
#     so first we will set base condition that if root is at end ie None return True
#     as it indicates full tree has been scanned and no False occurs
#     now we create two variables for comparison with root.val, which are minimum and maximum
#     we will scan the tree first by left side and then by right side both will validate
#     their own left subtrees and right subtrees
#     to validate on left we have to check root.val>root.left.val
#     and as we have minimum < root.val< maximum,
#     so as root moves downwards to left we will keep reassigning root to root.left
#     we will have to keep minimum always, and compare with root.val and max
#     so for each recursion root will be root.left and max will be root.val
#     Similarly for right subtrees, root will be root.right so root.val should be less than that 
#     so it will be assigned to minimum and maximum will stay max 
#     finally for whole tree we will assign max ani min as float('inf') and float('-inf')

        def validate(root,minimum, maximum):
            if not root: return True
            if not minimum < root.val< maximum: return False
            
            return validate(root.left, minimum,root.val) and validate(root.right,root.val,maximum)
        
        return validate(root,float('-inf'),float('inf'))
        
            