# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def solver(temp, root):
            nonlocal summ
            if root and not root.left and not root.right:
                path=int("".join(temp)+str(root.val))
                # print("path",path)
                summ+=path
                return 
            if root:
                temp.append(str(root.val))
                # print(temp)
                # print("to left")
                solver(temp,root.left)
                # print(temp)
                # print("to right")
                solver(temp,root.right)
                if temp: temp.pop()
                    
        summ=0
        solver([], root)
        return summ
        