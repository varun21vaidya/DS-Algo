# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def findPath(root, goal,ans):
            if not root: return False
                
            ans.append(root)
                
            if root.val==goal: return True
            
            if findPath(root.left, goal,ans) or findPath(root.right, goal,ans):
                return True
            else:
                ans.pop()
            
        pathp,pathq=[],[]
        findPath(root,p.val,pathp)
        findPath(root,q.val,pathq)   
        
        # print(pathp,pathq)
        
        i,j=0,0
        while i<len(pathp) and j < len(pathq):
            if pathp[i].val!=pathq[j].val:
                return pathp[i-1]
            i+=1
            j+=1
            
        if i==len(pathp): return pathp[-1]
        if j==len(pathq): return pathq[-1]
