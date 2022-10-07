# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n) -> List[Optional[TreeNode]]:
        
        
        def tree(start,n):
            bst=[]
            if start>n:
                bst.append(None)
                return bst

            for i in range(start,n+1):

                lefttree = tree(start,i-1)
                righttree = tree(i+1,n)

                for j in range(len(lefttree)):
                    for k in range(len(righttree)):
                        node=TreeNode(i)
                        left=lefttree[j]
                        right=righttree[k]

                        node.left=left
                        node.right=right

                        bst.append(node)

            return bst
        return tree(1,n)
                    