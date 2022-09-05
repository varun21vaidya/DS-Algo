"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        if root is None: return
        result=[]
        queue =collections.deque([root])
        
        while queue:
            level=[]
            for i in range(len(queue)):
                node= queue.popleft()
                level.append(node.val)
                # print(level)
                for child in node.children:
                    queue.append(child)
            result.append(level)
        return result
            
            