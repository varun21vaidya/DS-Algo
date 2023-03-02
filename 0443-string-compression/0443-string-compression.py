class Solution:
    def compress(self, chars: List[str]) -> int:
        
        #Brute force # inefficient
#         temp=1
#         s=""
#         if len(chars)==1:
#             return 1
#         for i in range(1, len(chars)):
            
#             if chars[i]==chars[i-1]:
#                 temp+=1
#             else:
#                 s+=chars[i-1]
#                 if temp>1:
#                     s+=str(temp)
#                 temp=1
#             # print(s,temp,i)
        
#         s+=chars[i]
#         if temp>1:
#             s+=str(temp)
#         chars[:]= list(s)
#         return len(chars)
                
    
        walker, runner = 0, 0
        while runner < len(chars):

            chars[walker] = chars[runner]
            count = 1

            while runner + 1 < len(chars) and chars[runner] == chars[runner+1]:
                runner += 1
                count += 1

            if count > 1:
                for c in str(count):
                    chars[walker+1] = c
                    walker += 1

            runner += 1
            walker += 1

        return walker
                