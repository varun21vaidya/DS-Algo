class SummaryRanges:

    def __init__(self):
        def cmp():
            return -1
        self.mp=defaultdict(cmp)
        self.a=[]
        

    def addNum(self, value: int) -> None:
        if self.mp[value]!=-1:
            return 
        if self.mp[value-1]!=-1:
            self.a.remove([self.mp[value-1],value-1])
            
            self.mp[value]=self.mp[value-1]
            self.mp[self.mp[value-1]]=value
            self.a.append([self.mp[value],value])
            if self.mp[value+1]!=-1:
                self.a.remove([self.mp[value],value])
                self.a.remove([value+1,self.mp[value+1]])
                self.a.append([self.mp[value],self.mp[value+1]])
                self.mp[self.mp[value]]=self.mp[value+1]
                self.mp[self.mp[value+1]]=self.mp[value]
                
        elif self.mp[value+1]!=-1:
            self.a.remove([value+1,self.mp[value+1]])
            
            self.mp[value]=self.mp[value+1]
            self.mp[self.mp[value+1]]=value   
            self.a.append([value,self.mp[value]])         
            
        if self.mp[value]==-1:
            self.mp[value]=value
            self.a.append([value,value])


    def getIntervals(self) -> List[List[int]]:
        return sorted(self.a)
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()