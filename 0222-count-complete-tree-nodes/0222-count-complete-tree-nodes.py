# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # # OBVIOUS BRUTE FORCE O(N)
        
#         def dfs(root,res):
#             if not root:return
#             res[0]+=1
#             dfs(root.left,res)
#             dfs(root.right,res)
        
#         if not root:return 0
#         res=[0]
#         dfs(root,res)
#         return res[0]


    # # For countnodes traverse: O(logN) and for left right traverse O(logN)
    # # Overall TC: O(logN * logN)
    
        def goleft(left):
            if not left: return 0
            self.l+=1
            goleft(left.left)
            
        def goright(right):
            if not right: return 
            self.r+=1
            goright(right.right) 
        
        
        if not root: return 0
        self.l,self.r=0,0
        goleft(root)
        goright(root)
        # print(self.l,self.r)

        if self.l==self.r:
            return (2**self.l)-1
        else:
            return 1+ self.countNodes(root.left)+self.countNodes(root.right)
            
        