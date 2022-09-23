class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        L=lcm(p,q)
        
        if (L//q)%2==0:
            return 2
        
        else: return (L//p)%2