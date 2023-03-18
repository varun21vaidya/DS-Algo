
# Two Stack Approach:

# class BrowserHistory:

#     def __init__(self, homepage: str):
#         self.store=[homepage] # stores incoming urls
#         self.future=[]  # does operations like forward and backword and returns output

#     def visit(self, url: str) -> None:
#         self.store.append(url)
#         # print(url,"added",self.store)
#         self.future=[]

#     def back(self, steps: int) -> str:
#         # print("go",steps,"steps backward", self.store)
#         while steps and len(self.store)>1:
#             self.future.append(self.store.pop())
#             steps-=1
        
#         return self.store[-1]
        

#     def forward(self, steps: int) -> str:
#         # print("go",steps,"steps forward",self.store)
#         while steps and self.future:
#             self.store.append(self.future.pop())
#             steps-=1 
#         return self.store[-1]
        

# Vector / ArrayList / Python List
# class BrowserHistory:

#     def __init__(self, homepage: str):
#         self.store=[homepage] # stores incoming urls
#         self.ind=0

#     def visit(self, url: str) -> None:
#         # print(url,"added",self.store)
#         if self.ind<len(self.store)-1:
#             self.store=self.store[:self.ind+1]
#         self.store.append(url)
#         self.ind+=1


#     def back(self, steps: int) -> str:
#         # print("go",steps,"steps backward", self.store)
#         if steps>self.ind:
#             self.ind=0
#         else:
#             self.ind=self.ind-steps
#         return self.store[self.ind]
            


#     def forward(self, steps: int) -> str:
#         # print("go",steps,"steps forward",self.store)
#         if len(self.store)-1-self.ind>=steps:
#             self.ind=self.ind+steps
#         else:
#             self.ind=len(self.store)-1
#         return self.store[self.ind]

class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
        self.prev=None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.dll=Node(homepage)

    def visit(self, url: str) -> None:
        # print(url,"added",self.store)
        self.newNode= Node(url)
        self.dll.next=self.newNode
        self.newNode.prev=self.dll
        self.dll=self.dll.next


    def back(self, steps: int) -> str:
        # print("go",steps,"steps backward", self.store)
        while steps and self.dll.prev:
            self.dll=self.dll.prev
            steps-=1
        return self.dll.data


    def forward(self, steps: int) -> str:
        # print("go",steps,"steps forward",self.store)
        while steps and self.dll.next:
            self.dll=self.dll.next
            steps-=1
        return self.dll.data
    

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)