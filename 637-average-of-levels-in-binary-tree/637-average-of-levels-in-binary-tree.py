# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
#         def getheight(root):
#             if root.left==None and root.right==None:
#                 return 0
#             left=0
#             if root.left!=None:
#                 left=getheight(root.left)
                
#             if root.right!=None:
#                 right=getheight(root.right)
                
#             return (max(left, right) +1)
                   
#         def calculate(node, level,ressum,resavg):
#             # global ressum
#             # global resavg
            
#             if node==None: return
#             if ressum[level]==0:
#                 levelnode=0
#             ressum[level]+=node.val
#             resavg[level]=ressum[level]/len(ressum)
#             print(ressum,level,len(ressum))
#             calculate(node.left, level+1,ressum,resavg)
#             calculate(node.right, level+1,ressum,resavg)

            
        
#         level=getheight(root)+1
#         ressum=[0]*level
#         resavg=[0]*level
#         # levelcount=0
#         print(level)
#         calculate(root, 0,ressum,resavg)
#         return resavg
        
        q=deque()
        q.append(root)
        ans =[]
        while q:
            qlen=len(q)
            row =0
            for i in range(qlen):
                node = q.popleft()
                row += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(row/qlen)
        return ans
        
        
        