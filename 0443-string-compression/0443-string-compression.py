class Solution:
    def compress(self, chars: List[str]) -> int:
        
        temp=1
        s=""
        if len(chars)==1:
            return 1
        for i in range(1, len(chars)):
            
            if chars[i]==chars[i-1]:
                temp+=1
            else:
                s+=chars[i-1]
                if temp>1:
                    s+=str(temp)
                temp=1
            # print(s,temp,i)
        
        s+=chars[i]
        if temp>1:
            s+=str(temp)
        # print(s)
        chars[:]= list(s)
        return len(chars)
                
            
            