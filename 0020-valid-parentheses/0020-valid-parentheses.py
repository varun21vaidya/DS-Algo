class Solution:
    def isValid(self, s: str) -> bool:
        
        stack=[]
        ref= {"(": ")","[":"]","{":"}"}
        for bracket in s:
            if not stack:
                stack.append(bracket)
            
            elif stack:
                last=stack[-1]
                if bracket in ref.keys():
                    stack.append(bracket)
                else:
                    if last in ref.keys() and ref[last]==bracket:
                        stack.pop()
                    else:
                        return False
                    
        if stack:
            return False
        else:
            return True
                        