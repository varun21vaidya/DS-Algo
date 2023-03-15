# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        # Criteria:
        # 1. should be left leaning, all left side should be filled first
        # 2. if root.left is none and root.right has value return false
        
        # DFS (NOT WORKING)
#         def solver(root):
#             if not root:
#                 return True
#             if not root.left and root.right:
#                 print(root.val)
#                 return False
#             if root:
#                 return solver(root.left) and solver(root.right)
            
#         return solver(root)
                
    # LEVEL ORDER TRAVERSAL
        q= deque([root])
        nullFound=False
        while q:
            for i in range(len(q)):
                temp= q.popleft()
                if not temp:
                    nullFound=True
                    continue
                if temp and nullFound:
                    return False
                q.append(temp.left)
                q.append(temp.right)

                

        return True

                
            
        
                    