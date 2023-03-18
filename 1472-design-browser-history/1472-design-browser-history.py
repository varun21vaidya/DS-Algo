class BrowserHistory:

    def __init__(self, homepage: str):
        self.store=[homepage] # stores incoming urls
        self.future=[]  # does operations like forward and backword and returns output

    def visit(self, url: str) -> None:
        self.store.append(url)
        # print(url,"added",self.store)
        self.future=[]

    def back(self, steps: int) -> str:
        # print("go",steps,"steps backward", self.store)
        while steps and len(self.store)>1:
            self.future.append(self.store.pop())
            steps-=1
        
        return self.store[-1]
        

    def forward(self, steps: int) -> str:
        # print("go",steps,"steps forward",self.store)
        while steps and self.future:
            self.store.append(self.future.pop())
            steps-=1 
        return self.store[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)