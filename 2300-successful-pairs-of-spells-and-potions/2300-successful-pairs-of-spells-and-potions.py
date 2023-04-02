class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        # TLE O(N+M+MlogM)
#         res=[0]*len(spells)
#         potions.sort()
#         for s,spell in enumerate(spells):
#             for p,potion in enumerate(potions):
#                 if spell*potion>=success:
#                     res[s]+=len(potions[p:])
#                     break
        
#         return res
    
        # Binary Search:
        def binarySearch(potions,target):
            low,high=0,len(potions)
            while low<high:
                mid=low+(high-low)//2
                if potions[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
            print(low)
            return low
        
        res=[0]*len(spells)
        l=len(potions)
        potions.sort()
        for s, spell in enumerate(spells):
            # x=binarySearch(potions,(success+spell-1)/spell)
            x= bisect_left(potions,ceil(success/spell))
            res[s]= l-x
            
        return res
        