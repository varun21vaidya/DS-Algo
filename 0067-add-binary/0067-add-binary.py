class Solution:
    def addBinary(self, a: str, b: str) -> str:
#         i,j=len(a),len(b)
#         if i>j:
#             b=('0'*(i-j))+b
#         else:
#             a=('0'*(j-i))+a
#         print(a,b)
#         res=""
#         extra=0
#         while i>=0:
#             x,y=0,0
#             if i>0: x,y=int(a[i-1]),int(b[i-1])
#             print("total is",extra+x+y)
#             if extra+x+y==2:
#                 if not extra: extra=1
#                 res="0"+res
#             elif extra+x+y==3:
#                 res="1"+res
#             else:
#                 res=str(extra)+res
#                 extra-=1
#             print(res)
#             i-=1
    
#        re res
        
            
        return bin(int(a, 2) + int(b, 2))[2:]    
            