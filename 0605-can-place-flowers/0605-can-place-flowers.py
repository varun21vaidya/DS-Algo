class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        size=len(flowerbed)
        if not n:
            return True
        if len(flowerbed)==1:
            if not flowerbed[0]:
                return True
            else:
                return False
        if not flowerbed[1] and not flowerbed[0]:
            flowerbed[0]=1
            n-=1
        if not flowerbed[size-2] and not flowerbed[size-1]:
            flowerbed[-1]=1
            n-=1
        for i in range(1,size-1):
            if n==0:
                return True
            if not flowerbed[i-1] and not flowerbed[i+1] and not flowerbed[i]:
                flowerbed[i]=1
                n-=1
            
        if n<=0:
            return True
        return False
            