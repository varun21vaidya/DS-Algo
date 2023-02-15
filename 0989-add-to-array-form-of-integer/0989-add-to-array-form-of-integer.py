class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        x= list(str(int("".join(str(x) for x in num))+k))
        return [int(y) for y in x]