# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        maxwd=0
        q= deque([[root,1]])
        while q:
            first,last=q[0][1],q[-1][1]
            for i in range(len(q)):
                temp,val=q.popleft()
                if temp.left: q.append([temp.left,val*2])
                if temp.right: q.append([temp.right,(val*2)+1])
            maxwd=max(maxwd,last-first+1)
        
        return maxwd

            