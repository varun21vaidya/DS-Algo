# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        

        def getTree(start, end):
            res=[]
            if start>end:
                res.append(None)
                return res
            
            for i in range(start,end+1):
                
                lefttrees=getTree(start, i-1)
                righttrees=getTree(i+1,end)
    
                for j in lefttrees:
                    for k in righttrees:
                    
                        left=j
                        right=k
                        
                        node=TreeNode(i)
                        node.left=left
                        node.right=right
                        
                        res.append(node)
            return res
        
        return getTree(1,n)