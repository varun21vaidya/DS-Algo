# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        
        def bfs(root):
            if not root: return 0
            q=deque([[root,1]])
            maxwidth, num=0,1
            while q:
                old=q[0][1]
                # print(q[0][0].val)
                for i in range(len(q)):
                    temp,num=q.popleft()
                    
                    if temp.left: q.append([temp.left,num*2])
                    
                    if temp.right: q.append([temp.right, num*2+1])

                maxwidth=max(maxwidth, num-old+1)
                
            return maxwidth
    
        return bfs(root)
                   
            