# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def addmap(root,parent):
             if not root: return

             mapp[root]=parent
             addmap(root.left,root)
             addmap(root.right,root)
        mapp=defaultdict(int)
        addmap(root,None)  


    # # USING DFS:

        # def solver(root,dist):
        #     if not root or root in visited :return
            
        #     visited.add(root)
        #     if dist==k:
        #         res.append(root.val)
        #         return
            
        #     solver(root.left,dist+1)
        #     solver(root.right,dist+1)
        #     solver(mapp[root],dist+1)

        # res=[]
        # visited=set()
        # solver(target,0)
        # return res

    # # USING BFS:
    
        q=deque([[target,0]])
        visited=set()
        visited.add(target)
        while q:
            # print("tree",[(node.val,d) for node, d in q])
            if q[0][1]==k: return [node.val for node, d in q]

            temp,dist= q.popleft()
            for node in (temp.left,temp.right,mapp[temp]):
                if node and node not in visited:
                    visited.add(node)
                    q.append([node,dist+1])
            # print("visited",[x.val for x in visited])

        return []
        