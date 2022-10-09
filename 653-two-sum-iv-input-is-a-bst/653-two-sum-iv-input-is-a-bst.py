# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
#         # Inorder Traversal and Two Pointer
        
#         def solver(root,lst):
#             if not root: return
#             solver(root.left,lst)
#             lst.append(root.val)
#             solver(root.right,lst)  
        
#         lst=[]
#         solver(root,lst)
#         # print(lst)
        
#         left,right=0,len(lst)-1
#         while left<right:
#             summ=lst[left]+lst[right]
#             if summ<k:
#                 left+=1
#             elif summ>k:
#                 right-=1
#             else:
#                 return True
#         return False



        def dfs(root,sett):
            if not root: return False
            
            diff= k-root.val
            if diff in sett: return True
            
            sett.add(root.val)
            return dfs(root.left,sett) or dfs(root.right,sett)
        
        return dfs(root, set())