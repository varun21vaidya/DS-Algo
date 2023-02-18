# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        # TC:O(n+n) SC: O(n)
        # def solver(root):
        #     if root:
        #         solver(root.left)
        #         res.append(root.val)
        #         solver(root.right)
        
        # res=[]
        # solver(root)
        # minn=float('inf')
        # for i in range(1,len(res)):
        #     minn=min(minn,res[i]-res[i-1])
        # return minn

        # TC: O(N) SC:O(1)+Stack Space of recursion
        # Improving Space Complexity
        def solver(root):
            if root:
                solver(root.left)
                nonlocal ans,prev
                ans=min(ans,root.val-prev)
                prev=root.val
                solver(root.right)

        ans,prev=float('inf'),float('-inf')
        solver(root)
        return ans
