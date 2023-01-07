# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
#         def solver(root, col,level):
#             if not root: return
            
#             mapp[col].append((level,root.val))
            
# #             if col in mapp:
# #                 if level in mapp[col]:
# #                     mapp[col][level].append(root.val)
# #                 else:
# #                     mapp[col][level]=[root.val]
                
# #             else:
# #                 mapp[col]={level: [root.val]}
            
#             solver(root.left,col-1,level+1)
#             solver(root.right,col+1,level+1)
        
#         mapp=defaultdict(list)
#         solver(root,0,0)
        
#         print(mapp)
#         # {0: {0: [1], 4: [6], 2: [10, 9]}, -1: {1: [2], 3: [5]}, -2: {2: [4]},
#         # 1: {1: [3]}, 2: {2: [10]}}
        
#         # after creating the data structure we will append those values in sorted order
#         ans=[]
# #         for col in sorted(mapp.keys()):
# #             temp=[]
# #             for level in sorted(mapp[col].keys()):
# #                 temp+=sorted(mapp[col][level])
# #             ans.append(temp)
        
# #         return ans   

# #---------------------------------------------------------------

        # METHOD 2:
    

        # but its not at all efficient cz two loops + sorted !!
        
        # so put everything in a single list and we will sort it

        def solver(root,col,level):
            if not root: return
        
            temp.append([col,level,root.val])
            
            solver(root.left, col-1,level+1)
            solver(root.right, col+1,level+1)
            
        temp=[]
        
        solver(root,0,0)
        temp.sort()
        # this is temp structure now: temp= [[col,level,val]]
        
        # print(temp)
            
        res=[[temp[0][2]]]
        for i in range(1,len(temp)):
            # if its same col as before add value to last added col
            if temp[i][0]==temp[i-1][0]:
                res[-1].append(temp[i][2])
            
            # else create new col list and add value
            else:
                res.append([temp[i][2]])
                
        return res
    
        