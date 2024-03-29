# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        def getheight(root):
            if root.left==None and root.right==None:
                return 0
            left=0
            if root.left!=None:
                left=getheight(root.left)
            right=0    
            if root.right!=None:
                right=getheight(root.right)
                
            return (max(left, right) +1)
               
            

        def calculate(node, level,ressum,resavg,levelcount):
            if node==None: return
            ressum[level]+=node.val
            levelcount[level]+=1
            resavg[level]=ressum[level]/levelcount[level]
            # print(ressum,level,levelcount)
            calculate(node.left, level+1,ressum,resavg,levelcount)
            calculate(node.right, level+1,ressum,resavg,levelcount)
        
        level=getheight(root)+1
        ressum=[0]*level
        resavg=[0]*level
        levelcount=[0]*level
        # print(level)
        calculate(root, 0,ressum,resavg,levelcount)

        return resavg
        

        
        
        