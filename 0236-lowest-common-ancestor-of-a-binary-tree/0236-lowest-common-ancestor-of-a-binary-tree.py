# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        # we will go to the path from root to each p and q
        # how will we do that, check this out
        # # Problem LINK: https://www.interviewbit.com/problems/path-to-given-node/

        # # Explanation:
        # # so first we will create a recursive function, and use it to traverse from left and then right and 
        # # then check if it meets the goal or not and store those nodes in between
        # # and if we observe that the further is deadend and we are returning without meeting goal 
        # # we remove such unnecessary nodes from our path

        # # Now first take the base condition, if root is Null return False
        # # and now append the node value to ans array
        # # and check if the root value is goal or not if we met goal return True
        # # then we will use boolean values for left and right traversal 
        # # if both of them are false both left and right traversals are useless
        # # so popout the last appended node
        # # but if any of them has met goal, that is correct path, so return True
        # # finally return the ans array path.
        
        
        # # now we got paths for q and q then from those paths we got that
        # # from root to some node both the paths were identical and at some point both saperated
        # # at this point is our common ancestor
        # # so we will traverse through both paths and check when they saperates ie their values differs
        # # so we will return node before that point

        # # But there are conditions like  a node to be a descendant of itself, in this case 
        # # one of the paths itself will end first so just return last node of that path
        
        
#         # TC: O(N) SC: O(N) # EXTRA SPACE COMPLEXITY USED FOR EACH PATH
        
#         def findPath(root, goal,ans):
#             if not root: return False
                
#             ans.append(root)
                
#             if root.val==goal: return True
            
#             if findPath(root.left, goal,ans) or findPath(root.right, goal,ans):
#                 return True
#             else:
#                 ans.pop()
            
#         pathp,pathq=[],[]
#         findPath(root,p.val,pathp)
#         findPath(root,q.val,pathq)   
        
#         # print(pathp,pathq)
        
#         i,j=0,0
#         while i<len(pathp) and j < len(pathq):
#             if pathp[i].val!=pathq[j].val:
#                 return pathp[i-1]
#             i+=1
#             j+=1
            
#         # when one of i, or j reaches end it means its last element was common node
#         if i==len(pathp): return pathp[-1]
#         if j==len(pathq): return pathq[-1]

        
        
        # # # IMPROVED VERSION - WITHOUT USING EXTRA SPACE
        
        # like we traversed left and right nodes, we will traverse again
        # but whenever we reach one of p or q, we will return that p or q
        # else we will return a null if we reach null
        # and at each node we will check if the returned node is null or p or q
        # if any one of them is null return other ie if left is null return right
        # now even if right is also null, we anyway had to return null
        # but if right has value of p or q, it will return that
        # now if left has value and right is null, return left
        # but if both of them has value then we have got the solution node
        # so return that node
        
        # But there are conditions like a node to be a descendant of itself, in this case 
        # suppose there is root node 3 on left there is 4 and right of it is 5-->6 and 
        # we had to find for 5 , 6 only, then from left 4 is not one of them, returns null
        # on right we got 5 which is one of them, so returns 5, and 3 will return 5 only
        # so if you observe, the code returns first occured p or q , and it will be LCA only.
        
        
        def solver(root):
            # if not root: return root # # ie return Null
            # if root==p: return p
            # if root==q: return q
            # # instead we can just combine them
            
            if not root or root==p or root==q:
                return root
            
            left=solver(root.left)
            right=solver(root.right)
            
            if not left: return right
            elif not right: return left
            else:
                return root
            
        return solver(root)
    
        
        