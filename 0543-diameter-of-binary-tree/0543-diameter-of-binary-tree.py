# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
#     # Explanation:

#     # Diameter of binary means maximum distance betwween two nodes
#     # IT doesnt need to be passed through root.
#     # The length of a path between two nodes is represented by the number of edges between them.
#     # so it indicates that our solution requires the combination of left and right lenghts to be maximum for any node
#     # so we can traverse and find for each node the depth of left subarray and depth of right subarray
#     # and calculate the maximum by comparing the result with left subarray and right subarray.

#     # TC: O(N*N) # Two recursive Functions
#         def maxheight(root):
#             if not root: return 0
            
#             left= maxheight(root.left)
#             right= maxheight(root.right)

#             return max(left,right)+1


#         if not root:
#             return 0
        
#         left= maxheight(root.left)
#         right= maxheight(root.right)

#         return max(left+right, self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
     
    
    
    
    
    # Modification:
    # as we saw depth calculate function is similar to main funciton
    # ie we are unnecessarily traversing the tree again in main function
    # instead we can just store the depth while traversing first time with a variable
    # and get maximum depth from each node, and
    # return the maximum length ie addition of  left and right 
    # TC: O(N) just one recursive function
    
    
        def helper(root,maxi):
            if not root: return 0

            left= helper(root.left,maxi)
            right= helper(root.right,maxi)
            maxi[0]=max(maxi[0],left+right)
            return max(left,right)+1

        maxi=[0]
        helper(root,maxi)
        return maxi[0]
