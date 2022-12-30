class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        # add 0 at beginning as its path as it will be present in all solutions
        # call the recursive function with 0 as current node, and target as final node
        # recursive function:
            # if current node is equal to target, add path to result and return
            # run a for loop traversing through elements of current node
            # add that node to path, and traverse recursively until we reach destination
            # pop the last added node, to backtrack properly 
            
        def solver(curr, path, target):
            
            if curr==target:
                ans.append(path[:])
                return
            
            for node in graph[curr]:
                path.append(node)
                solver(node, path, target)
                path.pop()
        
        ans=[]
        solver(0, [0], len(graph)-1)
        return ans