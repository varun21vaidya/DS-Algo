# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return
        q=deque([root])
        zig=True #(leftToRight)
        res=[]
        while q:
            level=[]
            for _ in range(len(q)):
                temp=q.popleft()
                if temp.left: q.append(temp.left)
                if temp.right: q.append(temp.right)
                
                level.append(temp.val)
            # print(zig)
            if zig:
                res.append(level)
            else:
                res.append(level[::-1])
            zig=not zig

        return res
            
            