# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
#         # Recursive Solution
#         def height(root):
#             if not root: return 0
            
#             left=height(root.left)
#             right=height(root.right)
            
#             return max(left,right)+1
        
#         return height(root)
            
        # BFS Solution ie Iterative Solution
        
        def height(root):
            q=deque([root])
            ans=0
            if not root:
                return ans
            while q:
                ans+=1
                for i in range(len(q)):
                    temp=q.popleft()
                    if temp.left:
                        q.append(temp.left)
                    if temp.right:
                        q.append(temp.right)
                
            return ans
        
        return height(root)
            

            
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        