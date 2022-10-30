class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        mostview={}
        maxview={}
        for i in range(len(creators)):
            if creators[i] in mostview:
                mostview[creators[i]]+=views[i]
                if views[i]==maxview[creators[i]][1]:
                    if maxview[creators[i]][0]>ids[i]:
                        # print(maxview[creators[i]][0],ids[i])
                        maxview[creators[i]][0]=ids[i]
                if views[i]>maxview[creators[i]][1]:
                    maxview[creators[i]]=[ids[i],views[i]]
            else:
                mostview[creators[i]]=views[i]
                maxview[creators[i]]=[ids[i],views[i]]
            
        m=max(mostview.values())
        maxcreators=[i for i,j in mostview.items() if j==m]
        # print(maxcreators)
        # print(maxview)
        res=[]
        for i in maxcreators:
            res.append([i, maxview[i][0]])
        # print(res)
        return res
            