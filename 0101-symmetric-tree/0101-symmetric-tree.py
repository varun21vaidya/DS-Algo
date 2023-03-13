# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

                    # Mirror property is    left == right and right == left
            # pre-order traversal on root->left subtree, (root, left, right)
            # modified pre-order traversal on root->right subtree, (root, right, left) 
            # compare the node val's if they are the same 
            # Do both traversals at the same time
            # if left is null or right is null, then both sides must match and return true (base case)
        def solver(left, right):
            # if one of the left or right is null other has to be null for symmetric
            if not left or not right:
                return left==right
            
            if left.val!=right.val:
                return False
            
            return solver(left.left , right.right) and solver(left.right, right.left)
    
        if not root: return False
        return solver(root.left, root.right)