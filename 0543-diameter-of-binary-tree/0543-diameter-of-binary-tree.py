# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
    # Explanation:

    # Diameter of binary means maximum distance betwween two nodes
    # IT doesnt need to be passed through root.
    # The length of a path between two nodes is represented by the number of edges between them.
    # so it indicates that our solution requires the combination of left and right lenghts to be maximum for any node
    # so we can traverse and find for each node the depth of left subarray and depth of right subarray
    # and calculate the maximum by comparing the result with left subarray and right subarray.

        def maxheight(root):
            if not root: return 0
            
            left= maxheight(root.left)
            right= maxheight(root.right)

            return max(left,right)+1


        if not root:
            return 0
        
        left= maxheight(root.left)
        right= maxheight(root.right)

        return max(left+right, self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
     
