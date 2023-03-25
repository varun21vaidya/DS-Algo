class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # Initialize parents and counts
        parents = list(range(n))
        counts = [1] * n
        
        # Define the find function using path compression
        def find(x):
            if parents[x] == x:
                return x
            parents[x] = find(parents[x])
            return parents[x]
        
        # Union find and update the counts
        for e in edges:
            ru = find(e[0])
            rv = find(e[1])
            if ru != rv:
                parents[rv] = ru
                counts[ru] += counts[rv]
        
        # Calculate the number of unreachable pairs
        ans = 0
        for i in range(n):
            ans += n - counts[find(i)]
        
        # Return the number of unreachable pairs
        return ans // 2