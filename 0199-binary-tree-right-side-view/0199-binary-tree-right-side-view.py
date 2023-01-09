# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        def dfs(root,col,level):
            if not root: return 
            
            mapp[level]=[col,root.val]
                
            dfs(root.left,col-1,level+1)
            dfs(root.right, col+1,level+1)
        
        mapp=defaultdict(list)
        dfs(root,0,0)
        # print(mapp)
        
        return [mapp[x][1] for x in mapp]


#         if not root: return
#         q=deque([root])
#         ans=[]
#         while q:
#             for i in range(len(q)):
#                 temp=q.popleft()
#                 if temp.left:
#                     q.append(temp.left)
#                 if temp.right:
#                     q.append(temp.right)
                
#             ans.append(temp.val)
#         return ans
            