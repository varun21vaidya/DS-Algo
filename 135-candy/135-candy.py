class Solution:
    def candy(self, ratings):
        count=0
        # res=[1 for i in range(len(ratings))]
        # changed=True
        # while changed:
        #     changed=False
        #     for i in range(len(ratings)):
        #         if i!=0 and ratings[i]>ratings[i-1] and res[i]<=res[i-1]:
        #             res[i]=res[i-1]+1
        #             changed=True
        #         if i!=len(ratings)-1 and ratings[i]>ratings[i+1] and res[i]<=res[i+1]:
        #             res[i]=res[i+1]+1
        #             changed=True
        # return sum(res)
    
        res,res2=[1 for i in range(len(ratings))],[1 for i in range(len(ratings))]
        res[0]=1
        res2[len(ratings)-1]=1
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                res[i]=res[i-1]+1
        # print(res)

        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                res2[i]=res2[i+1]+1
        # print(res2)
        
        final=0
        for i in range(len(ratings)):
            final+=max(res[i],res2[i])
        return final