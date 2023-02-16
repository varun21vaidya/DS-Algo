# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # BFS
#         if not root: return 0
#         q= deque([root])
#         counter=0
#         while q:
#             for _ in range(len(q)):
#                 temp= q.popleft()
                
#                 if temp.left: q.append(temp.left)
#                 if temp.right: q.append(temp.right)
                    
#             counter+=1
        
#         return counter

        # DFS
        def solver(root,counter):
            if not root: return counter
            counter+=1
            counter=max(solver(root.left,counter),solver(root.right,counter))
            
            return counter
            
        return solver(root,0)