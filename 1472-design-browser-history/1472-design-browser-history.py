class BrowserHistory:

    def __init__(self, homepage: str):
        self.store=[homepage] # stores incoming urls
        self.show=[]  # does operations like forward and backword and returns output

    def visit(self, url: str) -> None:
        self.store.append(url)
        # print(url,"added",self.store)
        self.show=[]

    def back(self, steps: int) -> str:
        # print("go",steps,"steps backward", self.store)
        while steps and len(self.store)>1:
            self.show.append(self.store.pop())
            steps-=1
        
        return self.store[-1]
        

    def forward(self, steps: int) -> str:
        # print("go",steps,"steps forward",self.store)
        while steps and self.show:
            self.store.append(self.show.pop())
            steps-=1 
        return self.store[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)