class TimeMap:

    def __init__(self):
        self.outermap={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.outermap:
            self.outermap[key]={}
            self.outermap[key][timestamp]= value
        else:
            self.outermap[key][timestamp]=value

    def get(self, key: str, timestamp: int) -> str:
        if key in self.outermap:
            for i in range(timestamp,0,-1):
                if i in self.outermap[key]:
                    return self.outermap[key][i]
        return ""
                
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)