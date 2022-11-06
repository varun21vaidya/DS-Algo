class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        
        
        # Using hashmap: O(n), O(n)
        # mapp=dict()
        # for i in nums:
        #     if i not in mapp:
        #         mapp[i]=1
        #     else:
        #         mapp[i]+=1
        # # print(mapp)
        # return [key for key,value in mapp.items() if value>n//3]
    
        candidate1=0
        candidate2=0
        count1=0
        count2=0
        for value in nums:
            if candidate1==value:
                count1+=1
            elif candidate2==value:
                count2+=1
            elif count1==0:
                candidate1=value
                count1=1
            elif count2==0:
                candidate2=value
                count2=1
            else:
                count1-=1
                count2-=1
        newcount1=0
        newcount2=0
        for count in nums:
            if candidate1==count:
                newcount1+=1
            elif candidate2==count:
                newcount2+=1
                
        res=[]
        
        if newcount1>n//3: res.append(candidate1)
        if newcount2>n//3: res.append(candidate2)
        
        return res