class Solution:
    def validUtf8(self, data: List[int]) -> bool:
 
# Initially convert each number to binary counterpart
# first check if remaining bytes are there or not
# if not then proceed and check if its a 1byte character ie byte[0]="0" then continue

# else run a loop from 0 to 8 to check 
# if 1st digit is 0 then return false as no such encoding exists
# else others like 2byte, 3byte, 4byte calculate remaining bytes to check and break
# if it shows byte remaining >=4 return false

# for remianing bytes check if first and second bits are 1 and 0 respectively and reduce remaining 
# else return false

# finally if remaining bytes is 0 return true else false

        remaining =0
        for byte in data:
            if byte>=255: return False
            byte=str(bin(byte)[2:])
            if len(byte)<8: 
                byte=str(0)*(8-len(byte))+byte
            # print(byte)
            
            if remaining==0:
                
                if byte[0]=="0": continue
                
                for i in range(8):
                    if byte[i]=="0":
                        if i==1: return False
                        
                        remaining=i-1
                        break
                if remaining>=4: return False
            
            elif remaining>0:
                if byte[0]!="1" or byte[1]!="0":
                    return False
                remaining-=1
                
        return True if (remaining==0) else False

        


            
            