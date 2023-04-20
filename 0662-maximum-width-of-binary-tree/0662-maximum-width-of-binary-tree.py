# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        q=deque()
        q.append([root,1])
        maxwidth=0
        while q:
            first,last=q[0][1], q[-1][1]
            for _ in range(len(q)):
                node,count=q.popleft()
                if node.left: q.append([node.left,count*2])
                if node.right: q.append([node.right,count*2+1])
                    
            maxwidth=max(maxwidth, last-first+1)
            
        return maxwidth
                    
        