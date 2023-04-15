# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
#         first as we can see we have to replace values on same level which are neighbours
#         so we will use BFS.
#         now we will also need such method to store the parent child relationship,
#         so that we can identify which child has same parents.
#         hence we can use map type object to store this relationship
        
#         and if we note that we just need the relationship for sum of all child values
#         of that parent, so we can use parent as key and sum of childs values as value
        
#         now for each level we will run a for loop over this map and get a total of 
#         all of its childs values and then again loop over each parent to get 
#         specific sum of its childs value, now to get sum of all of its neighbours
#         we can just remove this specific sum from total sum and
#         replace values of this parent with the calculated subtracted value.
        
        
#         TADA !! we have cracked logic of this problem, now its TIME TO CODE !!
        
        q=deque([root])
        ans=root # to return as final ans
        root.val=0 
        # first root will always be zero, just mentioning this is required.
        # because for its next level totalsum and specific sum will be same
        # and calculated value would be 0
        # and after that it will be piece of cake..
        
        # now lets start our bfs loop
        while q:
            
            # to make our life a little easier, we'll use defaultdict
            mapp= defaultdict(int)
            
            for _ in range(len(q)):
                node= q.popleft()
                
                if node.left:
                    q.append(node.left)
                    mapp[node]+=node.left.val
                    
                if node.right:
                    q.append(node.right)
                    mapp[node]+=node.right.val
                    
            
            # now time for calculations, first totalsum.
            
            totalsum=0
            for parent in mapp:
                totalsum+=mapp[parent]
                
            # now calculate for each parent's child value sum and subtract from totalsum.
            
            for parent in mapp:
                childsum=0
                
                if parent.left:
                    childsum+=parent.left.val
                if parent.right:
                    childsum+=parent.right.val
                
                res = totalsum-childsum
                
                if parent.left:
                    parent.left.val=res
                if parent.right:
                    parent.right.val=res
                    
        return ans
            
                
        
        
        