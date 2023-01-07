# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def solver(root, col,level):
            if not root: return
            
            if col in mapp:
                if level in mapp[col]:
                    mapp[col][level].append(root.val)
                else:
                    mapp[col][level]=[root.val]
                
            else:
                mapp[col]={level: [root.val]}
            
            solver(root.left,col-1,level+1)
            solver(root.right,col+1,level+1)
        
        mapp={}
        solver(root,0,0)
        
        # print(mapp)
        # {0: {0: [1], 4: [6], 2: [10, 9]}, -1: {1: [2], 3: [5]}, -2: {2: [4]},
        # 1: {1: [3]}, 2: {2: [10]}}
        
        # after creating the data structure we will append those values in sorted order
        ans=[]
        for col in sorted(mapp.keys()):
            temp=[]
            for level in sorted(mapp[col].keys()):
                temp+=sorted(mapp[col][level])
            ans.append(temp)
        
        return ans
            