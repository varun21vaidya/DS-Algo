# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        # recursive
#         def solver(inord,postord):
#             if not postord:
#                 return None
#             if len(postord)==1:
#                 # print(postord)
#                 return TreeNode(postord[-1])
#             root=TreeNode(postord[-1])
#             ind= inord.index(root.val)
#             # print(ind,inord,postord)
#             root.left=solver(inord[:ind],postord[:ind])
#             root.right=solver(inord[ind+1:],postord[ind:-1])
#             return root
    
#         return solver(inorder,postorder)

        # recursive without modifiying both arrays
        def solver(inst,inend,postst, postend):
            if postst>postend:
                return None
            if postst==postend:
                return TreeNode(postorder[postend])
            
            root=TreeNode(postorder[postend])
            ind= inorder.index(root.val)
            root.left=solver(inst, ind-1, postst, postst+(ind-inst)-1)
            root.right=solver(ind+1,inend,postst+(ind-inst),postend-1)
            
            
            return root
    
        return solver(0, len(inorder)-1,0, len(postorder)-1 )
    

            