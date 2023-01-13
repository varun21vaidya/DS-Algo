class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        graph= defaultdict(list)
        
        ans=1
        for i,value in enumerate(parent):
            graph[value].append(i)
            
        def dfs(node):
            nonlocal ans
            longest=next_longest=0
            
            for child in graph[node]:   
                pathlen= dfs(child)
               
                if s[child]!=s[node]:
                    if pathlen>longest:
                        next_longest=longest
                        longest=pathlen
                    elif pathlen>next_longest:
                        next_longest=pathlen

            ans= max(ans, longest+next_longest+1)
            return longest+1
        
        dfs(0)
        return ans