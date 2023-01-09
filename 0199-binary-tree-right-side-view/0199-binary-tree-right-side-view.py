# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # Iterative ie BFS: Intuiative
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
            
        # Recursive ie DFS 
        # take col and level ie grid like structure
        # and as we 
        def dfs(root,level):
            if not root: return 
            
            mapp[level]=root.val
                
            dfs(root.left,level+1)
            dfs(root.right,level+1)
        
        mapp=defaultdict(int)
        dfs(root,0)
        # print(mapp)
        
        return mapp.values()

        