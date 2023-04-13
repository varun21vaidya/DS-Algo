class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        popped.reverse()
        for push in pushed:
            stack.append(push)
            
            while stack and stack[-1]==popped[-1]:
                stack.pop()
                popped.pop()
                
                
        return len(stack)==0
            
                